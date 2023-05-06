# 메카니즘 핵 분열로

메카니즘 모드의 대량 에너지 생산 시설이다.

![asdf](../../asset/systems/mk_fission_reactor/main1.jpg)

![asdf](../../asset/systems/mk_fission_reactor/main2.jpg)

<!-- tag_target_open:frame:energy_generation_generations -->
:::tip 에너지 생산 시스템 변천사
화력 발전 -> [바이오(에틸렌) 발전](../systems/mk_ethylene_generator.md) -> [핵분열 원자로](../systems/mk_fission_reactor.md) -> 핵융합 원자로
:::
<!-- tag_close -->

결핍으로부터의 해방이라는 관점에선 핵융합로가 메카니즘의 엔드게임이라 볼 수 있으며, 핵분열로는 그 마지막 관문이다. 

틱당 최대 30mB의 핵연료를 사용할 수 있으며, 이 때의 발전량은 틱당 약 80만이다. 발전량만 보면 그냥 가스발전기 12대가 발전량, 안전성, 영구성, 난이도까지 다 씹어먹어버리지만 메카니즘의 마지막 컨텐츠들에 쓸 수 있는 핵 부산물을 얻을 수 있다는 점이 핵심이다.

핵분열로 운용에 있어 가장 까다로운 점은 크게 4가지가 있으며, 다음과 같은 방법으로 극복했다.
1. 만드는게 지랄맞다 : 황산 제조 라인을 별도로 분리한 덕에 Fissile Fuel 제조 공정을 엄청나게 단축시킬 수 있었다.

2. 연료를 계속 넣어줘야 한다 : Fissile Fuel을 보관할 수 있는 엄청난 용량의 다이내믹 탱크를 배치해서 연료의 원재료를 최대한 빠르게 처리한 뒤 탱크에 보관하는 방식을 사용했다. 덕분에 재료를 뭉탱이로 넣은 뒤 보관량-사용량을 저울질해서 관리가 비교적 쉽도록 했다. 현실적으로 채우는 건 불가능하지만, 탱크가 연료로 가득하다면 최대 발전량, 정상 틱레이트로도 원자로 가동을 현실 시간으로 18.5일간 유지할 수 있다.

3. 전기가 꽉 차면 터빈이 중지되고, 냉각수 순환이 멈춰 핵분열로가 터진다 : 저번 엔데버 서버에서 원자로를 한 번 날려먹었던 원인으로, 원자로 멜트다운의 가장 주된 원인이다. 위험 수준으로 원자로의 온도가 올라가면 작동을 멈추도록 간단한 회로를 배치했다.

4. 핵융합로만들면 이딴거다필요없는데ㅋㅋ : 팩트사용자를 서버에서 밴 처리하였다.

![asdf](../../asset/systems/mk_fission_reactor/sub1.jpg)

![asdf](../../asset/systems/mk_fission_reactor/sub2.jpg)

![asdf](../../asset/systems/mk_fission_reactor/energy_stae.jpg)

### 참여자
<!-- tag_source_open:link_list:member_contribute -->
- [BANJUHARA](../members/BANJUHARA.md)  
핵 분열로 설계 및 제작 / 유지보수
<!-- tag_close-->
