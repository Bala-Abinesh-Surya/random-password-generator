import { useState } from "react"

const defaultUserInputs = {
  length: 15,
  numbers: false,
  special: false
}

export default function UserInputs() {
  const [userInputs, setUserInputs] = useState(defaultUserInputs)

  const formOnChangeHandler = (event) => {
    if (event.target.name === "length") {
      setUserInputs({...userInputs, length: Number(event.target.value)})
    }
    else {
      // for the checkboxes
      setUserInputs({...userInputs, [event.target.name]: event.target.checked})
    }
  }

  return (
    <>
      <form onChange={formOnChangeHandler}>
        <div className="container col-3 mt-2">
          <label for="customRange1" class="form-label"><b>Password Length {userInputs.length}</b></label>
          <input type="range" name="length" class="form-range" id="customRange1" value={userInputs.length} min={15} max={30} />

          <div class="form-check">
            <input class="form-check-input" name="numbers" type="checkbox" value={userInputs.numbers} id="flexCheckDefault" />
            <label class="form-check-label" for="flexCheckDefault">
              Include Numbers
            </label>
          </div>

          <div class="form-check">
            <input class="form-check-input" name="special" type="checkbox" value={userInputs.special} id="flexCheckDefault" />
            <label class="form-check-label" for="flexCheckDefault">
              Include Special Characters
            </label>
          </div>
          <button className="btn btn-primary">Generate Password</button>
        </div>
      </form>
    </>
  )
}