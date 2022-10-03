

var pokiForm = document.querySelector('.pokiForm')

pokiForm.addEventListener('submit', function(e){
    e.preventDefault()
    // let pokiName = pokiForm.children[1].value
    let pokiName = document.querySelector('#pokiName').value
    console.log(pokiName);

    fetch(`https://pokeapi.co/api/v2/pokemon/${pokiName}`)    
        .then(resp => resp.json())
        .then(data => {
        // console.log(data.sprites.front_default)
        // do something with data
        var pokiHeading = document.querySelector('.pokiHeading')
        var pokiImg = document.querySelector('.pokiImg')

        pokiHeading.textContent = data.name
        pokiImg.innerHTML = `
        <img src="${data.sprites.front_default}" alt="">
        `
    })
    .catch(err => console.log(err))
})


