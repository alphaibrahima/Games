// const button = document.getElementById('btnValider')


var mot_de_passe = {}
var score = 0
function init(liste_mots) {
    
    
    document.getElementById("buttons").innerHTML = `<button type="submit" class="btn btn-primary" onclick="validateForm()">Valider</button>` 
    document.getElementById("score").innerText = score
    let p1 = new Promise((resolve, reject) => {
        var random_number = Math.floor(Math.random() * liste_mots.length)
        var random_word = liste_mots[random_number]
        // // console.log(random_number)
        // // console.log(random_word)
        mot_de_passe = {
            indices : [random_word.indice_1, random_word.indice_2, random_word.indice_3],
            solution : random_word.mot
        }
        resolve(mot_de_passe)
    })
    
    p1.then((mot_de_passe) => {   
        document.getElementById("indice").innerText = mot_de_passe.indices[0]
        document.getElementById("tentative").innerText = 1
        document.getElementById("icons").innerHTML = ''
        document.getElementById("msgFinal").innerText ="Top, c'est parti !!!" 
        cnt = 0   
        // console.log(mot_de_passe)
        // document.getElementById("indice").innerText = mot_de_passe.indices[0]
        // document.getElementById("tentative").innerText = 1
    });
    
}


// p2.then((liste_mots) => {
//     init(liste_mots)
// })

// {% for mot in liste_mots %}
//     console.log('{{ mot.mot }}')
// {% endfor %}

// document.getElementById("indice").innerText = mot_de_passe.indices[0]
// document.getElementById("tentative").innerText = 1

let cnt = 0 ;

function validateForm() {
    let reponse = document.getElementById("valider").value.toUpperCase();
    let mot = mot_de_passe.solution.toUpperCase()
    // console.log(reponse)
    // console.log(mot)

    if(cnt < 3 && reponse == mot){
        // alert("Bravo !!!")
        document.getElementById("valider").value =''
        document.getElementById("icons").innerHTML += `<div style="padding-top: 1rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-check-circle-fill" viewBox="0 0 16 16" style="
        color: lawngreen;">
        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
      </svg>
      </div>`
        document.getElementById("msgFinal").innerText ='Bravo !!!'
        document.getElementById("score").innerText = ++score
        document.getElementById("buttons").innerHTML = `
        <button type="submit" id="btnSubmit" class="btn btn-primary" onclick="validateForm()" >Valider</button>
        
        <button type="submit" class="btn btn-primary" onclick="init(liste)">Continuer</button>`
        
        document.getElementById("btnSubmit").disabled = true;
        
    }else if(cnt<3){
        // alert("Bof, tente encore.")
        document.getElementById("icons").innerHTML += `<div style="padding-top: 1rem;"> 
            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-x-circle-fill" viewBox="0 0 16 16" style="
            color: orangered;">
            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/>
        </svg>
        </div>`
        

        if(cnt<2){
            document.getElementById("msgFinal").innerText ='Bof, tente encore.'
            console.log(cnt)
            
            document.getElementById("score").innerText = score
            
        
            document.getElementById("valider").value =''
            document.getElementById("tentative").innerText = cnt+1
            document.getElementById("indice").innerText = mot_de_passe.indices[cnt+1]
            cnt++
        }else if( cnt==2){
            document.getElementById("msgFinal").innerText ="C'est dommage... Tu veux retenter ta chance ? Appuie sur le bouton 'Rejouer'"
            cnt++
            updateScore()

        }
        

    }

}

function reinit() {
    if(cnt>0){
        updateScore()
    }
    // console.log("Recommençons :)")
    // p3.then((liste_mots) => {
    init(liste)

    document.getElementById("btnSubmit").disabled = false
    // })
    // document.getElementById("indice").innerText = mot_de_passe.indices[0]
    // document.getElementById("tentative").innerText = 1
    // document.getElementById("icons").innerHTML = ''
    // document.getElementById("msgFinal").innerText ="Top, c'est parti !!!"
    document.getElementById("score").innerText = 0
    score = 0
    cnt=0
}



function updateScore(){
    var data = {'Score': score,
                'Joueur': joueur };
    $.post(URL, data, function(response){
        if(response === 'success'){ 
            // console.log('hello')
            // alert('Yay!');
         }
        else{ 
            // console.log('erreur')
            // alert('Error! :('); 
        }
    });
}

function addFeedback(){
    var data = {'Feedback': feedback};
    $.post(URL_feedback, data, function(response){
        if(response === 'success'){ 
            // console.log('hello')
            // alert('Yay!');
         }
        else{ 
            // console.log('erreur')
            // alert('Error! :('); 
        }
    });
}

// $(document).ready(function(){
//     $('#valider').click(function(){
//         updateScore();
//     });
//     // $('#bttnPlus').click(function(){
//     //     pieFact *= 1.1;
//     //     updatePieFact();
//     // });
// });