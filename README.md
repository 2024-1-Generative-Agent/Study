# Study

## 2024-1 Generative Agent 스터디를 위한 레포입니다.

> ### Generative_Agents
> - Generative Agents: Interactive Simulacra of Human Behavior 해당 논문 및 github 자료를 참고하였습니다.
> - original code: https://github.com/joonspk-research/generative_agents.git


## 20240629 수정사항
- maze.py - replace_gallery_pieces_all() 함수 추가
    - each reverive step마다 갤러리의 작품들의 변경 여부를 maze matrix에 반영합니다.
    - prev step과 current step의 작품이 다른 경우, updated event를 생성하여 반영합니다.
- maze.py - 초기 갤러리 작품 설명들 추가
    - backend_server/reverive/image_descrption.txt 파일에 저장, events tile을 통해 maze matrix에 반영합니다.
- 초기 이미지 삽입 및 이미지 수정은 가능한 상황이나, NPC가 직접 이미지 수정은 못하는 상황입니다.
- 따라서, 가상 세계 동작 도중의 이미지 수정은 사람이 하는 방향으로 하는 것이..

## Structure
>
> ### mapping
> - 우리의 프로젝트에 적용하기 위해 image 공간을 2D-matrix 및 trie 구조로 mapping하는데 사용한 코드 및 자료입니다.
>
> ### Presentation
> - 발표 자료로 사용했던 자료들입니다.


## Contributors
- Prometeus 5기 신우림 ([github](https://github.com/Rainwoorimforest))
- Prometeus 4기 유동균 ([github](https://github.com/yoodonggyun-github))
- Prometeus 3기 박은주 ([github](https://github.com/enjprk41))
- Prometeus 3기 모진호 ([github](https://github.com/JinhoMo))
- Prometeus 2기 김종효 ([github](https://github.com/naye971012))
