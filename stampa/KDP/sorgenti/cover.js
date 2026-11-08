const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{ const out=process.argv[2]; const [pw,ph,cw]=fs.readFileSync(path.join(out,'dims.txt'),'utf8').split(' ').map(Number);
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:Math.ceil(cw*96),height:Math.ceil(ph*96)},deviceScaleFactor:300/96});
 await p.goto('file://'+path.resolve(out,'copertina.html'),{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(800);
 await p.screenshot({path:path.join(out,'copertina-300dpi.png'),clip:{x:0,y:0,width:cw*96,height:ph*96}});
 await b.close(); })();
