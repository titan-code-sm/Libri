const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{ const out=process.argv[2]; const [pw,ph,cw]=fs.readFileSync(path.join(out,'dims.txt'),'utf8').split(' ');
 const b=await chromium.launch(); const p=await b.newPage();
 for (const [n,w] of [['interno',pw],['copertina',cw]]) {
  await p.goto('file://'+path.resolve(out,n+'.html'),{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(800);
  await p.pdf({path:path.join(out,`Sirena-Blu-KDP-${n}.pdf`),width:w+'in',height:ph+'in',printBackground:true,preferCSSPageSize:true});
 } await b.close(); })();
