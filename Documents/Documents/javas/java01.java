

/**
 * java01
 */
class Err{
    String msg;
    int code;
    Err(int s, String m){
        msg = m;
        code = s;
    }
    Err (int p){
    code = p;
    }
    Err (String madame){
        this.msg = madame;
    }
}
class ErrInfo{
    String[] error={
        "run time error",
        "compiler error",
        "exception error",
        "just an error"
    };
    int coded[] ={1,2,3,4};

    Err ErrInfomethod (int i) {
        if (i>=0 && error.length>0) {
            return new Err(coded[i], error[i]);
        }
        else return new Err(0, "invaid error code");
    }
}

 public class java01 {

    public static void main (String args[]){
        // there is there is there i sthere is there is 
        // god and he reigns in earth there is peace for the troubled SourceLanguagePositionthere id hipe for the troubled siol for the ones that are 
        // starving ther is hope for the ones that are starving he is he is he is God he is he is god he is god he is  god
        // jehovah jdk.internal.net.http
        // i want us to wordhiop God for just a while
        // ther is always a sound that precedes the move of God
        // sing this song and raise it as an offering to God
        // hallelujah you have won the victory
        // you have won it all for metal
        // death could not you are the reason  we 
        // hallelujah you have won the victoru 
        // you have won the victory
        // sitted in majestu
        // you are the reason we
        // you are the risen king 
        // sittedin majesty
        // desth could not hold you down
        // sitted in majesty you are the reason we 
        // risen king
        // that same spirit is in mw 
        // hallelujah
        // you have won the victory
        // we bless you omega we lift your name higher ika oka oyen keru wa i mela eze mo imela eze mo you are my lorsd and my healer and i bless your name imela 
        // the son of God is lifted high the son of God is lifted high ooo wonderful and glorious jesus jesus the son of God is lifted high ooo 
        // wonderful and glotuous jesus the son of God is ligted high the son of God is magnigied oh oh the son ogf God is magnigied ooooooo womderfil and glorious the son of God is magnified jesus the son of God is lifted high
        // seated in majesty you are the reason we hallelujah you areht e reason king seated in majesty death could not hold you back seated in makestu you are the readon king seated in majestu uou are the reason we hallelujah yoou are the reason king you are the reason king risen king halleluhag jallelujah you have won it all gor me halleluhaj you have won the victory you have won it all for it all for me7
        Err e;
        ErrInfo me = new ErrInfo();
        e = me.ErrInfomethod(2);
        System.out.println(e.msg);
        System.out.println(e.code);

    }
}