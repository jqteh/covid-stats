import React, {useState} from 'react';

export default function Region() {

    const [postCode, setPostCode] = useState(null)

    function handleChange(event) {
        const value = event.target.value;
        setPostCode(value);
    }

    return (
        <div>
            <input
                type="text"
                value={postCode}
                onChange={handleChange}
                className="postcode"
            />
        </div>
    )
}
