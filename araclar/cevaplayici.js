var clicked=0;

function cevapla(soru) {
    clicked+=1
    if (clicked>10) {
        document.getElementById("sonuc1").innerText="Yeter Artık Kullanıcı Adam Dur artık yeter bu kadar soru aaaaaa beynim yandı\nla";
        document.getElementById("sonuc1").style="font-size:20px;"
    }
    var number=Math.random(0,1);
    number=Math.round(number)
    
    if (number===0) {
        document.getElementById("sonuc").innerText=("HAYIR Diyorum")
    } else if (number===1) {
        document.getElementById("sonuc").innerText=("EVET Diyorum")
    }
    
}