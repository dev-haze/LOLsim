class Champ{//------------------------------------------------------------------------------champ
    // constructor(mana_stat, health_stat, skill_stat){
    //     this.m=mana_stat;
    //     this.h=health_stat;
    //     this.s=skill_stat;
    // }
    //          타입,체력,체젠,피흡률   방어막,물저,마저, 강인함(Tenacity)
    constructor(type, HP,HG,HS, Shield,AR,MR, tenacity,
                //마나,마젠,주문력,마관, 쿨탐,
                MP,MG, AP, ArPen, CoolT
                //평타공격력, 공속, 공격사거리, 치명타확률,치명타뎀
                
                  ){
        this.type = type;
    }

    Q(){
        //on/off 여부*
        //해당챔프스탯 변화*
        //사용 시 데미지
        
    }
    W(){

    }
    E(){

    }
    R(){

    }
    //---
    Atk(){//basic_atk

    }
    get_Atk(AD,AP){//hurt & cc;

    }

}


//------------------------------------------------------------------------------champ_code_res
class Champ_frame{
    constructor(type)

}
class Champ_hp_related_basic{
    constructor(){

    }
}
class Champ_resource_related_basic{
    constructor(resource_type,  )
}






/*<계산될 결과 종류>
        체력,체젠, 피흡률   방어막, 물저,마저, 강인함(Tenacity),
        마나,마젠, 기력, 기력젠, 분노, 쿨감,

        주문력, 쿨감, 마나, 마젠
        Q 쿨탐(쿨감 적용시), 공격력, (특수 : ex: 체젠, 도트딜, 방어막, 기타 능력치상승,  둔화,기절,속박,공포등cc지속시간)
        W 쿨탐(쿨감 적용시), 
        E 쿨탐(쿨감 적용시)
        R 쿨탐(쿨감 적용시)

        평타뎀,공속,공격사거리, 공격력, 치명타확률,치명타피해량, 방어구관통,마법관통

        아이템가속,스펠가속
        */
        /*<사용자가 설정할 수 있는 것>
        챔프레벨, 스킬레벨, 아이템, 룬, qwer특수효과적용여부 
        */
        //챔프
       //단순 데미지 판단용 더미(qwer,평에 반응. 피해량 보여줌. 기본스탯설정가능)
       //특정 챔프 더미
