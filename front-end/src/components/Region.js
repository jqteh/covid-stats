import React, {useState} from 'react';
import postCodeAreas from '../postcode-areas';

export default function Region(props) {

    const [postCode, setPostCode] = useState(null)
    const [region, setRegion] = useState("Cambridge")

    function handleChange(event) {
        const value = event.target.value;
        setPostCode(value);
        postCodeAreas.forEach( obj => {
            if (value === obj.postcodeArea) {
                setRegion(obj.region)
                props.endValue(obj.region);
            } 
        })
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
