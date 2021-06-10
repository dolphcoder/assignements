var num1 = 0, num2 = 0, op = '';
const scr = document.getElementById('screen');
document.querySelectorAll('.number').forEach(btn => {
    btn.addEventListener('click', (e) => {
        scr.innerText += e.target.innerText;
    })
})
document.querySelectorAll('.operator').forEach(btn => {
    btn.addEventListener('click', (e) => {
        num1 = parseInt(scr.innerText);
        op = e.target.innerText;
        scr.innerText = '';
    })
})
document.getElementById('equals').addEventListener('click', (e) => {
    num2 = parseInt(scr.innerText);
    switch (op) {
        case '+':
            scr.innerText = num1 + num2;
            break;

        case '-':
            scr.innerText = num1 - num2;
            break;

        case 'x':
            scr.innerText = num1 * num2;
            break;

        case '/':
            scr.innerText = num1 / num2;
            break;

        case '%':
            scr.innerText = num1 % num2;
            break;

        case '^':
            scr.innerText = num1 ** num2;
            break;
    }
})
document.querySelectorAll('.clear').forEach(btn => {
    btn.addEventListener('click', (e) => {
        if (e.target.innerText == 'AC') {
            num1 = 0;
            num2 = 0;
            op = '';
            scr.innerText = '';
        }
        else {
            if (scr.innerText.charAt(-1) == '+' || scr.innerText.charAt(-1) == '-' || scr.innerText.charAt(-1) == '*' || scr.innerText.charAt(-1) == '/' || scr.innerText.charAt(-1) == '%' || scr.innerText.charAt(-1) == '^') {
                op = '';
            }
            scr.innerText = scr.innerText.slice(0, -1);
        }
    })
})