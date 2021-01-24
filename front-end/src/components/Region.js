import React, {useState} from 'react';
import postCodeAreas from '../postcode-areas';
import _ from 'lodash';

export default function Region(props) {

    const [postCode, setPostCode] = useState(null)

    function handleChange(event) {
        const value = _.toUpper(event.target.value);
        setPostCode(value);
        postCodeAreas.forEach( obj => {
            if (value === obj.postcodeArea) {
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
