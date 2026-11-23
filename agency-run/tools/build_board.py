"""Build board_pages.html (owner preview of every page) from index.html.
Usage: python3 agency-run/tools/build_board.py index.html board_pages.html
index.html stays the launch file; this only produces a preview copy."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()

BOOT = "const params = (()=>{ try{ return new URLSearchParams(location.search); }catch(e){ return new URLSearchParams(''); } })();"
assert s.count(BOOT) == 1

BOARD_JS = r'''
/* ============================================================
   OWNER BOARD (preview build only; not in the launch file)
   ============================================================ */
const BOARD_PAGES = [
  ['A','sleep','وقت النوم'],['B','outings','الطلعات والزيارات'],['C','communication','التواصل'],
  ['D','food','الأكل'],['E','transitions','الآيباد والانتقال'],['F','emotions','الغضب والانفعال'],
  ['default','general','عامة (الإيميل)']
];
const BOARD_VIEWS = [['landing','صفحة الخطة'],['results','صفحة النتيجة'],['form','نموذج الانتظار'],['thanks','صفحة الشكر']];
const boardState = { key:'A', view:'landing' };
function boardAnswers(key){
  // sample answers: middle profile, weakest area = personalizing
  const a = {1:'A',2:'B',3:'B',8:'C', 4:'B',5:'C',7:'C',9:'C', 6:'B',10:'B',11:'C',12:'C', 13:'E'};
  a[14] = key==='default' ? {k:'G', text:'وقت الاستحمام'} : key;
  a[15] = 'يمر يومنا بهدوء أكثر، وأعرف ايش أسوي لما يصعب الموقف.';
  return a;
}
function boardRender(){
  document.querySelectorAll('.confetti').forEach(n=>n.remove());
  state.sent = true; state.lpPinged = true; state.wlPinged = true;
  state.name = 'سارة'; state.email = 'sara@example.com';
  state.answers = boardAnswers(boardState.key);
  const r = computeResults();
  if(boardState.key==='default'){ r.sitKey = 'G'; }
  renderResults(r);
  if(boardState.key==='default'){ applyLanding('default', r.primary, ''); }
  const v = boardState.view;
  setView(v);
  if(v==='thanks' && typeof confettiBurst==='function') confettiBurst();
  boardSync();
}
function boardSync(){
  document.querySelectorAll('[data-bk]').forEach(b=>b.setAttribute('aria-pressed', String(b.dataset.bk===boardState.key)));
  document.querySelectorAll('[data-bv]').forEach(b=>b.setAttribute('aria-pressed', String(b.dataset.bv===boardState.view)));
  const p = BOARD_PAGES.find(x=>x[0]===boardState.key);
  try{ history.replaceState(history.state, '', '#'+p[1]); }catch(e){}
}
function mountBoard(){
  const st = document.createElement('style');
  st.textContent = `
  .bd{background:#0E2E37;color:#F6F3EB;padding:12px max(14px,env(safe-area-inset-left,0px)) 12px;font-family:"Tajawal",sans-serif;direction:rtl}
  .bd-in{max-width:1080px;margin:0 auto;display:grid;gap:9px}
  .bd-t{font-family:"IBM Plex Sans Arabic","Tajawal";font-weight:700;font-size:15px;display:flex;justify-content:space-between;gap:10px;align-items:center}
  .bd-t small{font-family:"Tajawal";font-weight:500;font-size:12px;opacity:.7}
  .bd-row{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
  .bd-row::-webkit-scrollbar{display:none}
  .bd button{all:unset;cursor:pointer;white-space:nowrap;font-size:13.5px;font-weight:700;padding:7px 13px;border-radius:999px;
    border:1px solid rgba(246,243,235,.25);color:#F6F3EB}
  .bd button[aria-pressed="true"]{background:#C9935A;border-color:#C9935A;color:#2b1a08}
  .bd .bd-row.v button{font-weight:500;font-size:12.5px;padding:5px 11px}
  .bd .bd-row.v button[aria-pressed="true"]{background:#F6F3EB;border-color:#F6F3EB;color:#0E2E37;font-weight:700}
  .bd button:focus-visible{outline:2px solid #C9935A;outline-offset:2px}
  .bd-up{all:unset;position:fixed;bottom:calc(14px + env(safe-area-inset-bottom,0px));left:14px;z-index:70;cursor:pointer;
    background:#0E2E37;color:#F6F3EB;font-family:"IBM Plex Sans Arabic","Tajawal";font-weight:700;font-size:13px;padding:9px 14px;border-radius:999px;
    box-shadow:0 8px 20px -10px rgba(0,0,0,.5)}`;
  document.head.appendChild(st);
  const bar = document.createElement('div');
  bar.className = 'bd'; bar.setAttribute('role','navigation'); bar.setAttribute('aria-label','صفحات الموقع');
  bar.innerHTML = `<div class="bd-in">
    <div class="bd-t"><span>لوحة الصفحات</span><small>معاينة فقط، البيانات ما تنرسل</small></div>
    <div class="bd-row">${BOARD_PAGES.map(([k,,t])=>`<button type="button" data-bk="${k}">${t}</button>`).join('')}</div>
    <div class="bd-row v">${BOARD_VIEWS.map(([v,t])=>`<button type="button" data-bv="${v}">${t}</button>`).join('')}</div>
  </div>`;
  document.body.insertBefore(bar, document.body.firstChild);
  bar.addEventListener('click', e=>{
    const b = e.target.closest('button'); if(!b) return;
    if(b.dataset.bk){ boardState.key = b.dataset.bk; }
    if(b.dataset.bv){ boardState.view = b.dataset.bv; }
    boardRender(); window.scrollTo(0,0);
  });
  const up = document.createElement('button');
  up.className = 'bd-up'; up.type = 'button'; up.textContent = 'الصفحات ↑';
  up.addEventListener('click', ()=>window.scrollTo({top:0,behavior:'smooth'}));
  document.body.appendChild(up);
  const fromHash = ()=>{ const h = (location.hash||'').slice(1); const p = BOARD_PAGES.find(x=>x[1]===h); if(p) boardState.key = p[0]; };
  fromHash();
  addEventListener('hashchange', ()=>{ const k = boardState.key; fromHash(); if(k!==boardState.key) boardRender(); });
  boardRender();
}
'''
s = s.replace(BOOT, BOARD_JS + "\n" + BOOT, 1)

OLD_IF = "if(wantsLanding){"
assert s.count(OLD_IF) == 1
s = s.replace(OLD_IF, "if(true){ try{ sessionStorage.clear(); }catch(e){} mountBoard(); } else if(wantsLanding){", 1)
s = s.replace("<title>ليش نفس المواقف تتكرر مع طفلك؟ | مدار البيت</title>", "<title>صفحات مدار البيت</title>", 1)
open(dst, 'w').write(s)
print('built', dst)
