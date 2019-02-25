window.httpRequest = function (method, path, data, cb) {
  const xhr = new XMLHttpRequest()
  xhr.open(method, path, true)

  // Send the proper header information along with the request
  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')

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
  let incomeForm = document.getElementById('incomeForm')
  let expenseBtn = document.getElementById('expenseBtn')
  let expenseForm = document.getElementById('expenseForm')

  menuToggler.addEventListener('click', () => toggleSideMenu(menuToggler))

  incomeBtn.addEventListener('click', () => {
    showForm(incomeBtn, incomeForm)
    hideForm(expenseBtn, expenseForm)
  })

  expenseBtn.addEventListener('click', () => {
    showForm(expenseBtn, expenseForm)
    hideForm(incomeBtn, incomeForm)
  })

  showForm(expenseBtn, expenseForm)
  hideForm(incomeBtn, incomeForm)
}

function toggleSideMenu (button) {
  document.getElementById('wrapper').classList.toggle('toggled')
  button.classList.toggle('change')
}

function showForm (btn, form) {
  if (!btn.classList.contains('active')) btn.classList.toggle('active')

  form.style.display = ''
}

function hideForm (btn, form) {
  if (btn.classList.contains('active')) btn.classList.toggle('active')

  form.style.display = 'none'
}
