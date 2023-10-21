import React, { useState, useEffect } from "react";
import fetchDocument from "../api"

function DocumentView() {
    const [document, setDocument] = useState([])

    useEffect(() => {
        fetchDocument()
        .then((data) => {
            const formattedData = JSON.stringify(data, null, 2);
            setDocument(data)
        })
        .catch((error) => console.error("Error fetching data", error));
    }, []);

    return (
        <div>
            <pre>
                <code>{formattedData}</code>
            </pre>
        </div>
    );
}

export default DocumentView;
