const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const f of fs.readdirSync('out').filter(x=>x.endsWith('.html'))){await p.goto('file://'+process.cwd()+'/out/'+f);await p.waitForLoadState('networkidle');await p.evaluate(()=>document.fonts.ready);
const ok=await p.evaluate(()=>document.fonts.check('700 40px "El Messiri"'));await p.screenshot({path:'out/'+f.replace('.html','.png')});console.log(f,ok)}
await b.close()})();
