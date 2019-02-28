window.httpRequest = function (method, path, headers, data, cb) {
  const xhr = new XMLHttpRequest()
  xhr.open(method, path, true)

  for (var key in headers) xhr.setRequestHeader(key, headers[key])

  xhr.onreadystatechange = function () { // Call a function when the state changes.
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200 || xhr.status === 0) {
        cb(null, xhr.responseText)
      } else {
        let error = { statusCode: xhr.status, message: xhr.responseText }
        cb(error)
      }
    }
  }

  xhr.send(data)
}

window.onload = load

function load () {
  let menuToggler = document.getElementById('menu-toggle')
  let incomeBtn = document.getElementById('incomeBtn')
  let expenseBtn = document.getElementById('expenseBtn')
  let recordTypeInput = document.getElementById('recordType')
  let recordForm = document.getElementById('recordForm')
  let recordCards = document.getElementById('recordCards')

  menuToggler.addEventListener('click', () => toggleSideMenu(menuToggler))

  incomeBtn.addEventListener('click', () => {
    if (!incomeBtn.classList.contains('active')) {
      expenseBtn.classList.toggle('active')
      incomeBtn.classList.toggle('active')
    }

    recordTypeInput.value = 'Income'
  })

  expenseBtn.addEventListener('click', () => {
    if (!expenseBtn.classList.contains('active')) {
      expenseBtn.classList.toggle('active')
      incomeBtn.classList.toggle('active')
    }

    recordTypeInput.value = 'Expense'
  })

  recordForm.addEventListener('submit', event => {
    event.preventDefault()

    let formData = formToObject(recordForm)
    let headers = { 'X-CSRFToken': formData.csrfmiddlewaretoken, 'Content-type': 'application/json' }

    window.httpRequest(recordForm.method, recordForm.action, headers, JSON.stringify(formData), (err, body) => {
      if (err) return console.log(err)

      recordCards.innerHTML = body + recordCards.innerHTML
    })
  })
}

function formToObject (form) {
  let obj = {}
  let elements = form.querySelectorAll('input, select, textarea')
  for (var i = 0; i < elements.length; ++i) {
    let element = elements[i]
    let name = element.name
    let value = element.value

    if (name) obj[ name ] = value
  }
  return obj
}

function toggleSideMenu (button) {
  document.getElementById('wrapper').classList.toggle('toggled')
  button.classList.toggle('change')
}
