(function(){
  const $ = (s)=>document.querySelector(s);

  const state = {
    lang: localStorage.getItem('lbpo_lang') || (navigator.language||'en').slice(0,2),
    theme: localStorage.getItem('lbpo_theme') || 'system',
    consent: document.cookie.includes('lbpo_consent=1'),
  };
  if(!window.I18N[state.lang]) state.lang = 'en';
  document.documentElement.setAttribute('data-theme', state.theme);

  function t(k){ return (I18N[state.lang]||I18N.en)[k] || k; }

  function renderTexts(){
    $('#title').textContent = t('title');
    $('#desc').textContent  = t('desc');
    $('[data-i18n-task]').textContent = t('task');
    $('[data-i18n-backend]').textContent = t('backend');
    $('[data-i18n-apiKey]').textContent = t('apiKey');
    $('[data-i18n-model]').textContent = t('model');
    $('[data-i18n-evaluator]').textContent = t('evaluator');
    $('[data-i18n-iterations]').textContent = t('iterations');
    $('[data-i18n-beam]').textContent = t('beam');
    $('#casesTitle').textContent = t('cases');
    $('#casesHint').textContent = t('casesHint');
    $('#run').textContent = t('run');
    $('#bestTitle').textContent = t('best');
    $('#bestScoreLabel').textContent = t('bestScore');
    $('#artifactsLabel').textContent = t('artifacts');
    $('#boardTitle').textContent = t('leaderboard');
    $('#appearanceLabel').textContent = t('appearance');
    $('#langLabel').textContent = t('language');
    $('#rememberLabel').textContent = t('rememberKey');
    $('#footerTerms').textContent = t('footerTerms');
    $('#footerPrivacy').textContent = t('footerPrivacy');
    $('#footerCookies').textContent = t('footerCookies');
  }

  function populateLang(){
    const select = $('#lang');
    select.innerHTML='';
    Object.keys(I18N).forEach(code=>{
      const o=document.createElement('option');
      o.value=code; o.textContent=code.toUpperCase();
      if(code===state.lang) o.selected=true;
      select.appendChild(o);
    });
  }

  function initTheme(){
    $('#theme').value = state.theme;
    $('#theme').addEventListener('change', e=>{
      state.theme = e.target.value;
      document.documentElement.setAttribute('data-theme', state.theme);
      localStorage.setItem('lbpo_theme', state.theme);
    });
  }

  function initLang(){
    populateLang();
    renderTexts();
    $('#lang').addEventListener('change', e=>{
      state.lang = e.target.value;
      localStorage.setItem('lbpo_lang', state.lang);
      renderTexts();
    });
  }

  function initConsent(){
    if(state.consent) return;
    const banner = $('#cookieBanner');
    banner.style.display='flex';
    $('#cookieText').textContent = t('cookieMsg');
    $('#acceptBtn').textContent = t('accept');
    $('#declineBtn').textContent = t('decline');
    $('#acceptBtn').onclick = ()=>{
      document.cookie='lbpo_consent=1; Max-Age=31536000; Path=/';
      banner.style.display='none';
      state.consent = true;
    };
    $('#declineBtn').onclick = ()=>{ banner.style.display='none'; };
  }

  function initRemember(){
    try{
      if(localStorage.getItem('lbpo_api_key_saved')==='1'){
        $('#api_key').value = localStorage.getItem('lbpo_api_key')||'';
        $('#remember').checked = true;
      }
    }catch(e){}
    $('#remember').addEventListener('change', e=>{
      if(e.target.checked){
        if(!state.consent){ alert('Please accept cookies to store preferences.'); e.target.checked=false; return; }
        localStorage.setItem('lbpo_api_key_saved','1');
        localStorage.setItem('lbpo_api_key', $('#api_key').value.trim());
      }else{
        localStorage.removeItem('lbpo_api_key_saved');
        localStorage.removeItem('lbpo_api_key');
      }
    });
    $('#api_key').addEventListener('input', ()=>{
      if($('#remember').checked){
        localStorage.setItem('lbpo_api_key', $('#api_key').value.trim());
      }
    });
  }

  async function run(){
    const instruction = $('#instruction').value.trim();
    const backend = $('#backend').value;
    const api_key = $('#api_key').value.trim();
    const model = $('#model').value.trim();
    const evaluator = $('#evaluator').value;
    const iterations = parseInt($('#iterations').value,10)||3;
    const beam_width = parseInt($('#beam_width').value,10)||5;
    const raw = $('#cases').value.trim().split('\n').filter(Boolean);
    const testcases = raw.map(l=>{ const p=l.split('||'); return {input:(p[0]||'').trim(), expected:(p[1]||'').trim()}; });

    $('#run').disabled = true; $('#status').textContent = '...';
    try{
      const res = await fetch('/optimize', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({instruction, backend, api_key, model, evaluator, iterations, beam_width, testcases})
      });
      const data = await res.json();
      if(!res.ok){ $('#status').textContent = 'Error: ' + (data.error||res.status); $('#run').disabled=false; return; }
      $('#result').style.display='block'; $('#board').style.display='block';
      $('#best').textContent = data.best.prompt; $('#bestscore').textContent = data.best.score;
      $('#csv').href = data.artifacts.csv; $('#json').href = data.artifacts.json;

      const tbody = document.querySelector('#rows'); tbody.innerHTML='';
      (data.leaderboard||[]).forEach((row,i)=>{
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${i+1}</td><td>${row.score}</td><td><pre>${row.prompt.replaceAll('<','&lt;')}</pre></td>`;
        tbody.appendChild(tr);
      });
      $('#status').textContent = 'OK';
    }catch(e){ $('#status').textContent = 'Exception: '+e; }
    finally{ $('#run').disabled=false; }
  }

  // Bind & init
  document.querySelector('#run').addEventListener('click', run);
  initTheme(); initLang(); initConsent(); initRemember();
})();