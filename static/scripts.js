async function submitTest() {
    const textInput = document.getElementById("textInput").value;
    
    const response = await fetch("http://127.0.0.1:3001/tests/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: textInput })
    });

    const data = await response.json();
    alert(data.test);
    fetchTests();
}

async function fetchTests() {
    const response = await fetch("http://127.0.0.1:3001/tests/");
    const data = await response.json();
    
    const testList = document.getElementById("testList");
    testList.innerHTML = "";

    data.tests.forEach(test => {
        const li = document.createElement("li");
        li.textContent = `${test.text} (Sent: ${new Date(test.timeSent).toLocaleString()})`;
        testList.appendChild(li);
    });
}

document.addEventListener("DOMContentLoaded", fetchTests);

