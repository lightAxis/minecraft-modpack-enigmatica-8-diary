# 연혁

### 2023-04-15 첫 시작

### 2023-04-21 1차 모드 추가  

- create_central_kitchen
- create_crystal_clear
- create_enchantment_industry
- create_misc_and_things
- create_addition
- create_gear_addons
- create_steam_rails
- easy_villiagers

### 2023-04-23 서버 다이어리 사이트 탄생

서버 다이어리 사이트가 탄생했다.  
jasuk500이 관리하며, vuepress & github page로 제작했다.

### 2023-04-24 서버 롤백 사태  

갑자기 서버가 불안정해지더니, stop, spark tps를 쳐도 응답이 없어짐  
cpu 사용량이 600%(6코어 cpu이므로 사실상 전부)까지 올라감  
강제 종료 후 재부팅 했으나, 오버월드를 제외한 나머지 지역은 시간이 하루 전으로 돌아가있음.  
오버월드도 일부 부분의 컨피그나 세부 블럭 내용이 달라지거나 삭제되어 있었음.  
backup 주기를 2시간으로 늘리고, 백업 실패 메세지가 나올 시 반드시 관리자에게 알리도록 조치.  

### 2023-04-27 1차 다이어리 기록 제보

BANJUHARA, kidoxt 등이 `내가 한 일` 란에 내용과 이미지를 올렸다.  
github page는 한달 트래픽 한도가 100GB이므로 너무 많은 이미지는 좋지 않다.  
이미지의 용량이 너무 커짐에 따라, 무손실 압축인 .png-> 손실 압축 .jpg으로 바꿨으며
허용되는 이미지의 가로 최대 사이즈는 720px로 수정하였다. 
파이썬 스크립트로 해결하였다.

### 2023-04-28 길드 지하 몬스터 점령 사태

지하의 라이팅 시스템을 갈아엎겠다고 지하의 모든 광원을 제거한 탓에 몬스터가 대량으로 스폰된 사건.  
최근에 제작중인 시설들은 전부 집 지하에 있었는데, 텔레포터를 타고 들어온 사람들이 몬스터를 피해 도망다니며 혼비백산하는 사태가 벌어졌다. 
피해자중 한 명은 Flare Lantern을 숨겨서 설치해버리면 라이팅 시스템을 갈아엎지 못할것이라는 과격한 의견까지 제시하였다.  
Mega Torch를 사용하여 집을 포함한 주변의 모든 몬스터를 없앰으로써 사태는 일단락 되었다.  
### 2023-04-29 2차 모드 추가

- Stabx Modern Guns
- Modern Escalators & Elevators
- Framework
- CGM
- ExtraStorage