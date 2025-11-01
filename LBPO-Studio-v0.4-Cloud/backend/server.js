/**
 * Title: LBPO‑Studio v0.4 · Backend (Express)
 * Author: Tiger & Assistant
 * Description: Minimal API to simulate prompt optimization and return visualization data.
 */
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.get('/health', (req,res)=>res.json({ok:true, version:'v0.4'}));

app.post('/api/optimize', (req,res)=>{
  const { task = "Classify sentiment of a sentence; output POS or NEG only.", examples = "" } = req.body || {};
  function rnd(n){ return Math.random()*n }
  let acc = 52 + rnd(8), f1 = acc - 2 + rnd(3), pass = acc - 4 + rnd(6);
  const steps = [
    { name: "Explicit output schema", boost: 4 + rnd(2.5) },
    { name: "Few-shot from examples", boost: 5 + rnd(3) },
    { name: "Short CoT reasoning", boost: 3 + rnd(2) },
    { name: "Negative constraints", boost: 2 + rnd(1.5) },
    { name: "Self-check verifier", boost: 4 + rnd(2.5) },
  ];
  const labels = [], series = [], barsL = [], barsV = [];
  steps.forEach((s, i)=>{
    acc = Math.min(100, acc + s.boost);
    f1 = Math.min(100, f1 + s.boost*0.9);
    pass = Math.min(100, pass + s.boost*0.85);
    labels.push(`v${i+1}`);
    series.push(Math.round(acc));
    barsL.push(s.name);
    barsV.push(Math.round(s.boost*10)/10);
  });
  const best = [
    "You are a precise assistant.",
    `Task: ${task}`,
    "Rules:",
    "1) Output the exact required format only.",
    "2) Think briefly, then output final answer only.",
    "3) If uncertain, choose safest default."
  ].join("\n");
  res.json({
    acc: Math.round(acc),
    f1: Math.round(f1),
    pass: Math.round(pass),
    cost: 100 - Math.round(rnd(25)),
    labels, series, barsL, barsV, best,
    versions: labels.map((l,i)=>`${l} · ${barsL[i]} · +${barsV[i]}%`).join("\n"),
    progress: Math.round((acc-50)/0.5)
  });
});

const PORT = process.env.PORT || 10000;
app.listen(PORT, ()=>{
  console.log(`LBPO‑Studio v0.4 backend listening on :${PORT}`);
});
