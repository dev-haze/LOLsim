class champ_basic_status{
    constructor(){
        var hp = new stat_res();
        var hpgen = new stat_res();
    
        var atk_dmg = 1;
        var atk_spd = 1;
        var atk_dst = 1;
        var crit_per = 1;
        var crit_dmg = 1;

        var spd = 1;
    }  
}


class stat_res{
    constructor(){
        this.remain=1;
        this.regen=1;
    }
}