# v2/index.html에서 v3/index.html을 만든다. 바뀐 것: 공식에 첫 결제 금액과 재결제를 넣음.
# 실행: python3 v3/make.py v2/index.html v3/index.html
import sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src,encoding='utf-8').read()
def rep(old,new,count=1):
    global s
    n=s.count(old)
    assert n==count,(n,old[:80])
    s=s.replace(old,new)

rep('<meta property="og:url" content="https://bk-nam.github.io/cercle-landing/v2/">','<meta property="og:url" content="https://bk-nam.github.io/cercle-landing/v3/">')

# 1단계: 공식 끝에 금액과 재결제
rep('<h2>다음 예약을 잡고<br>다시 오시는 분까지<br>셉니다.</h2><p class="sub">다시 오신 분은 광고비 없이 온 매출입니다.</p>',
    '<h2>결제하신 분이<br>여섯 달 동안 쓰시는 돈까지<br>셉니다.</h2><p class="sub">첫 결제 55.7만 원에, 다음 예약을 잡고 다시 오셔서 재결제하신 금액까지 더합니다. 그러면 광고비 100만 원이 여섯 달 매출 약 750만 원이 됩니다.</p>')

# 2단계 여는 말
rep('<h2>그다음, 광고비는<br>그대로 두고<br>결제를 늘립니다.</h2><p class="sub">보통 관리가 안 된 곳이 있어서, 여기서 먼저 오릅니다.</p>',
    '<h2>그다음, 광고비는<br>그대로 두고<br>결제를 늘립니다.</h2><p class="sub">결제하시는 분 수와 첫 결제 금액, 재결제를 같이 늘립니다. 보통 관리가 안 된 곳이 있어서, 여기서 먼저 오릅니다.</p>')

# 놓친 결제에 '회차가 끝나 가는 분' 추가
rep('<p class="sub">상담하고 결제를 미룬 분, 예약으로 안 이어진 문의부터.</p>',
    '<p class="sub">상담하고 결제를 미룬 분, 예약으로 안 이어진 문의, 남은 회차가 두세 번인 분부터.</p>')
rep('<div class="card" style="--i:4"><div class="row"><div><div class="nm">다음 예약에 안 오신 분</div>','<div class="card" style="--i:5"><div class="row"><div><div class="nm">다음 예약에 안 오신 분</div>')
rep('<div class="card" style="--i:3"><div class="row"><div><div class="nm">다음 예약 없이 가신 분</div>','<div class="card" style="--i:4"><div class="row"><div><div class="nm">다음 예약 없이 가신 분</div>')
rep('<div class="card" style="--i:2"><div class="row"><div><div class="nm">예약하고 안 오신 분</div>',
    '<div class="card" style="--i:2"><div class="row"><div><div class="nm">남은 회차가 두세 번인 분</div><div class="sb">41명, 상담실장이 재결제 상담</div></div><span class="amt num" data-n="2000" data-pre="약 " data-suf="만 원">약 2,000만 원</span></div></div>\n'
    '            <div class="card" style="--i:3"><div class="row"><div><div class="nm">예약하고 안 오신 분</div>')

# 아침 명단
rep('<span class="sb">결제를 미룬 고객 10명</span>','<span class="sb">결제를 미룬 고객 7명, 남은 회차가 두 번인 고객 3명</span>')

# 결제 명수 다음 장면: 금액과 재결제
ylift2='''
    <div class="step" data-step="ylift2">
      <div class="cap"><div class="pillrow"><span class="pill">8/15</span><span class="pname">2단계 결제 늘리기</span></div><h2>첫 결제 금액과<br>재결제도<br>같이 오릅니다.</h2><p class="sub">광고비 100만 원이 여섯 달 동안 가져온 매출이 약 750만 원에서 약 1,020만 원이 됩니다.</p></div>
      <div class="frame" data-frame="ylift2">
        <div class="fit">
          <div class="cards seq">
            <div class="card" style="--i:0;gap:12px">
              <span class="nm">관리 전</span>
              <div class="kv"><span>광고비 100만 원당 결제</span><span>11.0명</span></div>
              <div class="kv"><span>한 분의 첫 결제</span><span>55.7만 원</span></div>
              <div class="kv"><span>여섯 달 안에 재결제하신 분</span><span>18%, 평균 70만 원</span></div>
              <div class="kv"><span>100만 원당 여섯 달 매출</span><span>약 750만 원</span></div>
            </div>
            <div class="card" style="--i:1;gap:12px">
              <span class="nm">결제를 미룬 분, 회차가 끝나 가는 분까지 챙긴 뒤</span>
              <div class="kv"><span>광고비 100만 원당 결제</span><span>13.2명</span></div>
              <div class="kv"><span>한 분의 첫 결제</span><span>60만 원</span></div>
              <div class="kv"><span>여섯 달 안에 재결제하신 분</span><span>25%, 평균 70만 원</span></div>
              <div class="kv"><span>100만 원당 여섯 달 매출</span><span><mark class="hl">약 1,020만 원</mark></span></div>
              <span class="sb">결제하신 분은 20%, 매출은 36% 늘었습니다.</span>
            </div>
          </div>
        </div>
        <p class="note">예시입니다. 오르는 폭은 의원마다 다르고, 약속하는 값이 아닙니다.</p>
      </div>
    </div>
'''
rep('\n    <div class="step" data-step="scale">', ylift2+'\n    <div class="step" data-step="scale">')

# 매일 아침 카톡
rep('<span style="--i:5">다음 예약을 잡고 가신 분은 18명입니다.</span>','<span style="--i:5">남은 회차가 두세 번인 고객 41명 중 23명이 재결제했습니다.</span>')

# 3년 뒤
rep('<h2>그렇게 매달<br>하루 한두 명씩 늘면,<br>3년 뒤 월매출 4억입니다.</h2></div>',
    '<h2>그렇게 매달<br>하루 한두 명씩 늘면,<br>3년 뒤 월매출 4억입니다.</h2><p class="sub">내원 한 번에 결제가 18만 원에서 20만 원이 되면, 하루 80명이면 닿습니다.</p></div>')

open(dst,'w',encoding='utf-8').write(s)
print('ok',len(s))
