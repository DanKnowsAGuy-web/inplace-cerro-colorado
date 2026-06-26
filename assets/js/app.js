// Tab switching and CBR bar animation for the bilingual report.
function animBars(scope){
  (scope||document).querySelectorAll('.tr-bar').forEach(function(b){
    b.style.width=(b.getAttribute('data-w')||0)+'%';
  });
}
document.querySelectorAll('.tab-btn').forEach(function(btn){
  btn.addEventListener('click',function(){
    var id=btn.getAttribute('data-tab');
    document.querySelectorAll('.tab-btn').forEach(function(b){b.classList.remove('active');});
    document.querySelectorAll('.tab-panel').forEach(function(p){p.classList.remove('active');});
    btn.classList.add('active');
    document.getElementById(id).classList.add('active');
    animBars(document.getElementById(id));
    // Land on the tabs bar (not the page top) so it stays a pinned header
    // and the freshly selected panel begins directly underneath it.
    var tabsBar=document.querySelector('.tabs-bar');
    if(tabsBar){window.scrollTo({top:tabsBar.offsetTop,behavior:'instant'});}
  });
});
setTimeout(function(){animBars(document.getElementById('enfull'));},200);
