import React, { useState, useEffect } from "react";
import fetchDocument from "../api"

function DocumentView() {
    const [document, setDocument] = useState([])

    useEffect(() => {
        fetchDocument()
        .then((data) => setDocument(data))
        .catch((error) => console.error("Error fetching data", error));
    }, []);

    return (
        <div>
            <pre>
                <code>{JSON.stringify(document, null, 2)}</code>
            </pre>
        </div>
    );
}

export default DocumentView;
