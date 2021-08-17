let form = document.getElementById('id_form')
let name = document.getElementById('id_name')
let phone = document.getElementById('id_phone')
let alert = document.getElementById('alert_message')
let csrf = document.getElementsByName('csrfmiddlewaretoken')

//insert message about sending
function alert_fun(text, color) {
    alert.innerHTML = text
    alert.style.color = color
}

// send message to database by AJAX
form.addEventListener('submit', e => {
    e.preventDefault()
    const url = ''
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('name', name.value)
    fd.append('phone', phone.value)

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function(response) {
            alert_fun('Сообщение успешно отправлено!', '#00ff00')
            setTimeout(() => {
                name.value = ""
                phone.value = ""
            }, 100);
        },
        error: function(error) {
            alert_fun('Сообщение не отправлено!', '#ff2400')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

//pages animations, scroll, add blocks
document.addEventListener('scroll', () => {

    let adv = document.querySelector('.advantages');
    let repair = document.querySelector('.we-repair');
    let height = document.documentElement.clientHeight
    let rect = adv.getBoundingClientRect();
    let rep = repair.getBoundingClientRect();

    if (rect.y < (height - 200)) {
        adv.style.opacity = '1'
    }

    if (rep.y < (height - 200)) {
        repair.style.opacity = '1'
    }
})

let href = document.querySelectorAll('.menu a')
let count = 0;
let delay = 200;

for (let i = 0; i < href.length; i++) {
    setTimeout(function time(delay) {
        href[i].style.opacity = '1';
    }, delay)
    delay = delay + 300;
}

