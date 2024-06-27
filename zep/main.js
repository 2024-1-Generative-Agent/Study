class system {
  constructor() {
    this.sprite_sheet_list = ["sprite000.png"];
  }
}

const _npcs = [];

class buildNPC {
  constructor(name, x, y) {
    if (name) this.name = name;
    else this.name = "NPC";

    if (x) this.x = x;
    else this.x = 0;

    if (y) this.y = y;
    else this.y = 0;

    this.caller = "";

    this.property = {
      key: this.name,
      moveSpeed: 80,
      useDirAnim: true,
      impassable: true,
      collide: true,
      offsetX: -8,
      offsetY: -32,
      oberlap: false,
      npcProperty: { name: this.name },
    };

    this.load_sprite("sprite000.png");

    this.build();
  }

  build() {
    Map.putObjectWithKey(this.x, this.y, this.sprite, {
      overlap: true,
      movespeed: 50,
      key: this.name,
      collide: true,
      useDirAnim: true,
      offsetX: -8,
      offsetY: -32,
      collide: true,
    });

    this.updateProperty();
    this.getLoc();
  }

  load_sprite(spriteName) {
    this.sprite = App.loadSpritesheet(
      spriteName,
      48,
      64,
      {
        left: [5, 6, 7, 8, 9], // 좌방향 이동 이미지
        up: [15, 16, 17, 18, 19],
        down: [0, 1, 2, 3, 4],
        right: [10, 11, 12, 13, 14],
        dance: [
          20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
          37,
        ],
        down_jump: [38],
        left_jump: [39],
        right_jump: [40],
        up_jump: [41],
      },
      10
    );
  }

  updateProperty() {
    this.property = Map.getObjectWithKey(this.name);
    return this.property;
  }

  //   get location of npc
  getLoc() {
    this.updateProperty();
    let { tileX, tileY } = this.property;

    this.x = tileX;
    this.y = tileY;

    return { x: this.x, y: this.y };
  }

  sayBallon(message) {
    Map.sayObjectWithKey(this.name, message);
  }

  sayToAll(message) {
    App.sayToAll(`[ ${this.name} ] ${message}`, 0xe0e0e0);
  }

  move(x, y) {
    return Map.moveObjectWithKey(this.name, x, y, true);
  }

  responseToPlayer(text) {
    let numbers = text.split(" ");

    // 배열의 각 요소를 숫자로 변환하여 x와 y에 할당
    let x = parseInt(numbers[0], 10);
    let y = parseInt(numbers[1], 10);

    this.move(x, y);

    // this.sayToAll(text);
    this.sayBallon(`(${x}, ${y})로 이동합니다.`);
  }

  //   // A* 알고리즘으로 최적 경로 계산
  // function calculatePath(start, end, obstacles) {
  //     // 경로 계산 로직 구현
  //     // ...
  //     // 임시적으로 현재 위치에서 목표 위치로 직선 경로를 반환하는 예시를 작성합니다.
  //     var path = [];
  //     var deltaX = end.x - start.x;
  //     var deltaY = end.y - start.y;
  //     var stepX = deltaX > 0 ? 1 : -1;
  //     var stepY = deltaY > 0 ? 1 : -1;
  //     var x = start.x;
  //     var y = start.y;

  //     while (x !== end.x || y !== end.y) {
  //         if (x !== end.x) {
  //             x += stepX;
  //         }
  //         if (y !== end.y) {
  //             y += stepY;
  //         }
  //         if (!isObstacle(x, y, obstacles)) {
  //             path.push({ x: x, y: y });
  //         } else {
  //             // 장애물이 있는 경우, 이동 중지
  //             break;
  //         }
  //     }

  //     return path;
  // }

  // // 특정 위치가 장애물인지 확인하는 함수
  // isObstacle(x, y) {
  //     let isValid =
  //     Map.getTile(2, x, y) === 0 &&
  // }

  destruct() {
    Map.putObjectWithKey(this.x, this.y, null, { key: this.name });
  }

  chatGPT_parse(url, body, callback) {
    App.httpPostJson(url, {}, body, (res) => {
      App.sayToAll(`${res}`, 0xffffff);
      // 요청 결과를 JSON 오브젝트로 변환
      let response = JSON.parse(res);
      App.sayToAll(`보낸 데이터: ${response.data.name}`, 0xffffff);
    });
  }
}

App.onInit.Add(function () {
  //NPC 추가
  _npcs.push(new buildNPC("테스터", 21, 48));
});

App.onSay.add(function (player, text) {
  //말해보기
  for (let npc of _npcs) {
    npc.responseToPlayer(text);
  }
});

App.onUpdate.Add(function (dt) {
  //위치 얻기
  for (let npc of _npcs) {
    npc.getLoc();
  }
});

App.onDestroy.Add(function () {
  //모든 오브젝트 제거
  Map.clearAllObjects();
});
