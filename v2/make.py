import re,sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src,encoding='utf-8').read()
def rep(old,new,count=1):
    global s
    n=s.count(old)
    assert n==count,(n,old[:80])
    s=s.replace(old,new)
def cut(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)+len(end)
    s=s[:i]+new+s[j:]
def cap(pill,pname,h2,sub=None):
    return ('<div class="cap"><div class="pillrow"><span class="pill">%s/15</span><span class="pname">%s</span></div><h2>%s</h2>%s</div>'
            %(pill,pname,h2,('<p class="sub">%s</p>'%sub) if sub else ''))

DESC='3년 뒤 월매출 4억. 매달 하루 한두 명씩 더 오시게 하는 피부과 경영 시스템, 세르클.'
rep('<meta name="description" content="매출을 예측 가능하게. 경영 파트너 세르클이 돕습니다.">','<meta name="description" content="%s">\n<meta name="robots" content="noindex">'%DESC)
rep('<meta property="og:description" content="매출을 예측 가능하게. 경영 파트너 세르클이 돕습니다.">','<meta property="og:description" content="%s">'%DESC)
rep('<meta property="og:url" content="https://bk-nam.github.io/cercle-landing/">','<meta property="og:url" content="https://bk-nam.github.io/cercle-landing/v2/">')

# hero
rep('<h1>매출을<br>예측 가능하게.</h1>','<h1>3년 뒤 월매출 4억.<br>매달 하루 한두 명이면 됩니다.</h1>')
rep('aria-label="결제 한 건을 거꾸로 따라가기"','aria-label="3년 뒤 4억에서 광고비 공식까지"')

# new layers in story A
GOAL='''<div class="gs hide" data-g="%s">
            <div class="gc">
              <div class="rc-top"><span>3년 계획</span><span>예시</span></div>
              <div class="kv"><span>지금 월매출</span><span>1.9억 원</span></div>
              <div class="kv"><span>지금 하루 내원</span><span>42명</span></div>
              <div class="kv"><span>내원 한 번에 결제</span><span>평균 18만 원</span></div>
              <hr>
              <div class="kv"><span>3년 뒤 목표 월매출</span><span>4억 원</span></div>
              <div class="kv ev"><span>그때 필요한 하루 내원</span>%s</div>
              <div class="kv ev"><span>매달 늘릴 하루 내원</span>%s</div>
            </div>
            <p class="rc-cap">%s</p>
          </div>
          '''
gq=GOAL%('goalq','<span class="bx">?</span>','<span class="bx focus">?</span>','하루에 몇 명이 더 오셔야 할까요?')
ga=GOAL%('goala','<span>89명</span>','<span class="bx full focus">1.3명</span>','다음 달 43명, 그다음 달 44명. 36개월 동안 이렇게만 가면 됩니다.')
rep('<div class="gs hide" data-g="ad">', gq+ga+'<div class="gs hide" data-g="ad">')
rep('<div class="gp" style="--i:1"><span>이벤트 가격</span><b>39만 원</b></div>','<div class="gp" style="--i:1"><span>다음 달 두 배면</span><b>2,800만 원</b></div>')
rep('<div class="gp" style="--i:0"><span>광고비</span>','<div class="gp" style="--i:0"><span>지난달 광고비</span>')
rep('<p class="rc-cap">지난달만큼 쓰면 될까요?</p>','<p class="rc-cap">다음 달은 두 배로 써도 될까요?</p>')
rep('<p class="rc-cap c-shut">넣은 돈이 어떻게 매출이 되는지 보이지 않습니다.</p>','<p class="rc-cap c-shut">광고비 1,400만 원이 결제 몇 명이 됐는지 모릅니다.</p>')
rep('<p class="rc-cap c-open">광고비는 알아보기부터 상담까지 네 단계를 거쳐 매출이 됩니다.</p>','<p class="rc-cap c-open">광고비는 문의, 예약, 상담을 거쳐 결제가 됩니다. 단계마다 세면 됩니다.</p>')
rep('<span class="t14">상담 당일 결제율이 5%p 오르면 약 790만 원이 더 들어옵니다.</span>','<span class="t14">광고비는 그대로 두고 상담 당일 결제율만 5%p 올려도, 한 달 약 790만 원이 더 들어옵니다.</span>')

# story A steps
A=[('goalq',cap(2,'목표','3년 뒤<br>월매출 4억이 되려면,<br>하루에 몇 명이 더<br>오셔야 할까요?')),
   ('goala',cap(2,'목표','매달 하루 한두 명씩.<br>그거면 됩니다.','지금 하루 42명이면 3년 뒤 89명. 한 달에 하루 1.3명씩 늘면 닿습니다.')),
   ('g1',cap(3,'광고','하루 한두 명 더 늘리는<br>가장 확실한 방법은<br>광고입니다.','그런데 다음 달 광고비를 두 배로 늘리지는 못하십니다.')),
   ('g3',cap(3,'광고','광고비가 결제 몇 명으로<br>돌아오는지 모르니까요.','밑 빠진 독에 물 붓는 것 같아서, 확신이 서지 않습니다.')),
   ('g4',cap(4,'1단계 공식 찾기','그래서 먼저<br>광고비와 결제 사이의<br>공식부터 찾습니다.')),
   ('q1',cap(4,'1단계 공식 찾기','결제 한 건에<br>상담이 몇 건 필요한지 세고,')),
   ('q2',cap(4,'1단계 공식 찾기','상담 한 건에<br>예약이 몇 건,')),
   ('q3',cap(4,'1단계 공식 찾기','예약 한 건에<br>문의가 몇 건 필요한지 세면,')),
   ('q4',cap(4,'1단계 공식 찾기','결제 1건에<br>광고비 9.1만 원.<br>100만 원이면 결제 11명.','이게 이 의원의 공식입니다.')),
   ('q5',cap(4,'1단계 공식 찾기','경로마다 결제 1건에 드는<br>광고비가 다릅니다.','네이버 검색은 15만 원, 인스타그램은 30만 원.')),
   ('q6',cap(4,'1단계 공식 찾기','다음 예약을 잡고<br>다시 오시는 분까지<br>셉니다.','다시 오신 분은 광고비 없이 온 매출입니다.')),
   ('filled',cap(5,'2단계 결제 늘리기','그다음, 광고비는<br>그대로 두고<br>결제를 늘립니다.','보통 관리가 안 된 곳이 있어서, 여기서 먼저 오릅니다.')),
  ]
stepsA='<div class="steps">\n'+'\n'.join('    <div class="step%s" data-step="%s">%s</div>'%('' if i==0 or A[i-1][1].split('pname">')[1].split('<')[0]!=c.split('pname">')[1].split('<')[0] else ' sub',k,c) for i,(k,c) in enumerate(A))+'\n  </div>\n</section>'
i=s.index('id="story-a"'); j=s.index('<div class="steps">',i); k=s.index('</section>',j)+len('</section>')
s=s[:j]+stepsA+s[k:]

# LAD entries
rep("    trend: { rows: [0,1,2,3,4,5,6], layer: 'chart' }","    trend: { rows: [0,1,2,3,4,5,6], layer: 'chart' },\n    goalq: { rows: [], layer: 'goalq' }, goala: { rows: [], layer: 'goala' }")

# story B
rep('aria-label="세르클을 쓰면 달라지는 하루와 한 달"','aria-label="결제를 늘리고, 광고비를 늘리고, 되풀이하기"')
i=s.index('id="story-b"'); j=s.index('<div class="steps">',i)+len('<div class="steps">'); 
# keep leak and today frames from original
orig=s
def frame(name):
    a=orig.index('<div class="frame" data-frame="%s">'%name)
    b=orig.index('<p class="note">',a); b=orig.index('</div>',b)+len('</div>')
    return orig[a:b]
leak=frame('leak'); today=frame('today'); morning=frame('morning')
morning=morning.replace('<span style="--i:2">초진 상담 11명 중 8명이 당일 결제했습니다.</span>','<span style="--i:2">지난주 광고비 100만 원당 결제 13.1명</span>')
morning=morning.replace('<span style="--i:3">다음 예약을 잡고 가신 분은 18명입니다.</span>','<span style="--i:3">초진 상담 11명 중 8명이 당일 결제했습니다.</span>')
morning=morning.replace('<span style="--i:4">11월 목표 2억 원 중 3,190만 원을 채웠습니다.</span>','<span style="--i:4">이번 달 하루 평균 내원 44명, 계획보다 1명 많습니다.</span>')
morning=morning.replace('<span style="--i:5">남은 21일 동안 하루 800만 원씩이면 됩니다.</span>','<span style="--i:5">다음 예약을 잡고 가신 분은 18명입니다.</span>')
assert '100만 원당' in morning and '계획보다' in morning
ylift='''<div class="frame" data-frame="ylift">
        <div class="fit">
          <div class="cards seq">
            <div class="card" style="--i:0;gap:12px">
              <span class="nm">관리 전</span>
              <div class="kv"><span>결제 1건에 드는 광고비</span><span>9.1만 원</span></div>
              <div class="kv"><span>광고비 100만 원당 결제</span><span>11.0명</span></div>
            </div>
            <div class="card" style="--i:1;gap:12px">
              <span class="nm">결제를 미룬 분과 문의부터 챙긴 뒤</span>
              <div class="kv"><span>결제 1건에 드는 광고비</span><span>7.6만 원</span></div>
              <div class="kv"><span>광고비 100만 원당 결제</span><span><mark class="hl">13.2명</mark></span></div>
              <span class="sb">같은 광고비에 결제가 20% 늘었습니다.</span>
            </div>
          </div>
        </div>
        <p class="note">예시입니다. 오르는 폭은 의원마다 다르고, 약속하는 값이 아닙니다.</p>
      </div>'''
scale='''<div class="frame" data-frame="scale">
        <div class="fit">
          <div class="cards seq">
            <div class="card" style="--i:0;gap:12px">
              <span class="nm">광고비를 늘려 가며 공식을 봅니다</span>
              <div class="tbl">
                <div class="tr th"><span>한 달 광고비</span><span>100만 원당 결제</span><span>결제</span></div>
                <div class="tr"><span>1,400만 원</span><span>13.2명</span><span>185명</span></div>
                <div class="tr"><span>2,100만 원</span><span>13.0명</span><span>273명</span></div>
                <div class="tr"><span>2,800만 원</span><span>12.1명</span><span>339명</span></div>
                <div class="tr"><span>3,500만 원</span><span><mark class="hl">10.4명</mark></span><span>364명</span></div>
              </div>
              <span class="sb">2,800만 원에서 3,500만 원으로 더 쓴 700만 원에는 결제가 25명, 100만 원당 3.6명만 늘었습니다. 여기서 멈추고 다시 2단계로 갑니다.</span>
            </div>
          </div>
        </div>
        <p class="note">예시입니다. 경로마다 따로 셉니다.</p>
      </div>'''
years='''<div class="frame" data-frame="years">
        <div class="fit plan">
          <div class="seq" style="display:flex;flex-direction:column">
            <div class="prow" style="--i:0"><span class="nm">지금</span><span class="t20">하루 42명, 월 1.9억 원</span></div>
            <div class="cn" style="--i:1"><i></i><b>매달 하루 1.3명씩</b></div>
            <div class="prow" style="--i:2"><span class="nm">1년 뒤</span><span class="t20">하루 58명, 월 2.6억 원</span></div>
            <div class="cn" style="--i:3"><i></i><b>매달 하루 1.3명씩</b></div>
            <div class="prow" style="--i:4"><span class="nm">2년 뒤</span><span class="t20">하루 73명, 월 3.3억 원</span></div>
            <div class="cn" style="--i:5"><i></i><b>매달 하루 1.3명씩</b></div>
            <div class="prow ink" style="--i:6"><span class="nm">3년 뒤</span><span class="t20">하루 89명, 월 4억 원</span></div>
          </div>
        </div>
        <p class="note">예시. 한 달 25일 진료, 내원 한 번에 평균 18만 원으로 셈했습니다. 약속하는 값이 아닙니다.</p>
      </div>'''
B=[('leak',cap(8,'2단계 결제 늘리기','놓친 결제를<br>금액이 큰 순서로 챙깁니다.','상담하고 결제를 미룬 분, 예약으로 안 이어진 문의부터.'),leak),
   ('today',cap(8,'2단계 결제 늘리기','누가 누구에게 연락할지<br>매일 아침 명단으로 옵니다.','실장과 데스크는 명단대로 전화하고 문자하면 됩니다.'),today),
   ('ylift',cap(8,'2단계 결제 늘리기','광고비 100만 원에<br>결제 11명이던 것이<br>13명이 됩니다.','광고비는 한 푼도 더 쓰지 않았습니다.'),ylift),
   ('scale',cap(9,'3단계 광고비 늘리기','그다음에<br>광고비를 늘립니다.','100만 원당 결제가 다시 줄기 시작하면 멈춥니다.'),scale),
   ('morning',cap(10,'4단계 되풀이','2단계와 3단계를<br>되풀이합니다.','공식이 그대로인지 매일 아침 8시 카톡으로 받습니다.'),morning),
   ('years',cap(11,'3년 뒤','그렇게 매달<br>하루 한두 명씩 늘면,<br>3년 뒤 월매출 4억입니다.'),years)]
stepsB='\n'+'\n'.join('''    <div class="step" data-step="%s"%s>
      %s
      %s
    </div>
'''%(k,' id="today"' if k=='today' else '',c,f) for k,c,f in B)+'\n  </div>\n</section>'
k=s.index('</section>',j)+len('</section>')
s=s[:j]+stepsB+s[k:]

# close
rep('<span class="pname">최고의 매출 관리 시스템</span>','<span class="pname">세르클</span>')
rep('<h2>매출을 예측 가능하게.</h2>','<h2>3년 뒤 월매출 4억.</h2>')
rep('<p class="sub">경영 파트너 세르클이 돕습니다.</p>','<p class="sub">공식을 찾고, 결제를 늘리고, 광고비를 늘리는 일을 세르클이 매달 같이 합니다.</p>')
for a,b in [('1 데일리 브리핑','1 공식 찾기'),('2 잠재 기회 확인','2 결제 늘리기'),('3 명료한 행동','3 광고비 늘리기'),('4 예측 가능한 성과','4 줄면 멈추기'),('5 다음 달 경영계획','5 다시 2단계로')]:
    rep('>'+a+'<','>'+b+'<')
rep('<p class="loop-c">이 고리가 돌 때마다<br>매출이 올라갑니다.</p>','<p class="loop-c">한 바퀴 돌 때마다<br>하루 내원이 늘어납니다.</p>')
rep('aria-label="다섯 단계를 한 바퀴 돌 때마다 한 단계씩 위로 올라가는 나선"','aria-label="공식 찾기, 결제 늘리기, 광고비 늘리기, 줄면 멈추기, 다시 2단계로. 한 바퀴 돌 때마다 위로 올라가는 나선"')
open(dst,'w',encoding='utf-8').write(s)
print('ok',len(s))
