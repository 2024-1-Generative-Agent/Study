class buildNPC{
    constructor(){
        this.name = "진호";
        this.level = 1;
        this.hp = 100;
        this.mp = 100;
        this.attack = 10;
        this.defense = 10;
    }

    show_level(){
	App.sayToAll(`[info]${this.name} has entered.`, 0x00ffff); // 하늘색으로 표시하기
    }
}

App.onInit.Add(function () {
    const npc = new buildNPC();
    npc.show_level();
});