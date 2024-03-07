import UserInputs from "./UserInputs"

export default function DisplayPassword() {
  return (
    <>
      <div className="container mt-5 text-center">
        <div className="container mt-5">
          <h3>Password Generator</h3>
          <span>Generate a random and secure password and save yourself a headache!</span>

          <UserInputs />
        </div>
      </div>
    </>
  )
}