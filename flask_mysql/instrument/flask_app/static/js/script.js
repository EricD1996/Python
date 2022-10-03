var instrumentForm = document.querySelector('#instrument-form')

instrumentForm.addEventListener('submit', function(e){
    e.preventDefault()

    var form = new FormData(instrumentForm)
    form.append('something', 'the value')

    fetch('/api/instrument/create', {
        method: 'post',
        body: form
    })
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        let instrumentTableBody = document.querySelector('#instrument-table-body')
        instrumentTableBody.innerHTML += `
        <tr>
            <td>${data.resp_data.name}</td>
            <td>${data.resp_data.fullname}</td>
            <td>
                <a href="/instrument/${data.resp_data.id}/edit">Edit</a>
                <a class="text-danger"href="/instrument/${data.resp_data.id}/delete">Delete</a>
            </td>
        </tr>
        `
    })
    .catch(err => console.log(err))
})