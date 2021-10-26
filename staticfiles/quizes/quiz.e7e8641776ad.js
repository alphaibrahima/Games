console.log('quizzz')
const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const scorebox = document.getElementById('score-box')
const resultbox = document.getElementById('result-box')


$.ajax({
	type: 'GET',
    url: `${url}data`,
    success: function (response){
        //console.log(response)
        const data = response.data
        data.forEach(el =>{
            for (const [question, answers] of Object.entries(el)){
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer=>{
                    quizBox.innerHTML += `
                    <hr>
                    <div>
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <label for="${question}">${answer}</label>
                    </div>
                `
                })
            }
        });
    },
    error: function (error){
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response){
            const results= response.results
            quizForm.classList.add('not-visible')
            
            scorebox.innerHTML=`${response.passed ? 'congratulations !':'Ups..:('} Yout result is ${response.score}%`
            console.log(response.score)
            results.forEach(res=>{
                const resDiv= document.createElement("div")
                for(const [question, resp] of Object.entries(res)){
                    
                    resDiv.innerHTML+=question
                    const cls= ['container', 'p-3', 'text-light', 'h3']
                    resDiv.classList.add(...cls)
                    
                    if(resp == 'not answered'){
                        resDiv.innerHTML += ' | not answerd'
                        resDiv.classList.add('bg-danger')
                    }

                    else{
                        const answer= resp['answered']
                        const correct= resp['correct_answer']
                        
                        if(answer == correct){

                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML+='answered : '+answer

                        }

                        else
                        {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML+='| Correct answer : '+correct
                            resDiv.innerHTML+='| answered : '+answer
        

                        }
                        console.log(answer, correct)
                    }

                }
                //const body=document.getElementsByTagName('BODY')[0]
                resultbox.append(resDiv)

            })

        },
        error: function (error){
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})