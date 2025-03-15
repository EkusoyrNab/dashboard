async function fetchData() {
    const response = await fetch("http://localhost:5000");
    const data = await response.json();

    document.getElementById("payments").innerHTML = data.payments.map(p =>
        `<li>${p.項目}: ${p.金額}円 (支払日: ${p.支払日})</li>`
    ).join("");

    document.getElementById("tasks").innerHTML = data.tasks.map(t =>
        `<li>${t.タスク} - ${t.日付}</li>`
    ).join("");
}

window.onload = fetchData;

