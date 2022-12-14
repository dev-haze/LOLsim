export default class Champ_stat{
    constructor(){
        this.hp = [1,1];//[능력치, 성장 능력치]
        this.hpgen=[1,1];
        this.mp=[1,1];
        this.mpgen=[1,1];

        this.atk_dmg=[1,1];
        this.atk_spd=[1,1];
        this.atk_dst= 1;

        this.p_resist=[1,1];
        this.m_resist=[1,1];

        this.spd = 1;

        this.items= new Array();
    }
}