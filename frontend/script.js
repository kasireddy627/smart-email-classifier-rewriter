async function classifyEmail() {

    const email = document.getElementById("classifyEmail").value;

    const response = await fetch(
        "http://127.0.0.1:8000/classify_email",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email
            })
        }
    );

    const data = await response.json();

    document.getElementById("classificationResult").innerText =
    data.category;
}

async function rewriteEmail() {

    const email = document.getElementById("rewriteEmail").value;
    const tone = document.getElementById("tone").value;

    const response = await fetch(
        "http://127.0.0.1:8000/rewrite_email",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                tone: tone
            })
        }
    );

    const data = await response.json();

    document.getElementById("rewriteResult").value =
    data.rewritten_email;
}