//레지스터 메인에 대신 쓰고 있음 
import React, { useCallback, useState } from "react"
import {Link} from "react-router-dom";
import styled from "styled-components";
import { useInput } from "../../hook/useInput";

const SendMain = () => {
    const [email,onChangeUserEmail] = useInput("");
    const [name, onChangeUserName] = useInput("");
    const [password, onChangeUserPassword] = useInput("");

    const [confirmPassword, setConfirmPassword] = useState("");
    const [passwordCheckMessage, setPasswordCheckMessage] = useState(false);

    const onChangeConfirmPassword = useCallback(
        (event) => {
            setConfirmPassword(event.target.value);
            setPasswordCheckMessage(event.target.value !== password);
        },
        [password]
    )

    return (
        <>
            <RegisterForm>
                <h1>메일 문의</h1>   
                <div>
                    <label htmlFor="user-name"></label>
                    <input 
                    name="user-name" 
                    type="text" 
                    placeholder="Enter your name" 
                    value={name} 
                    onChange={onChangeUserName}
                    required
                    />
                </div>
                <div>
                    <label htmlFor="user-id"></label>
                    <input 
                    name="user-email" 
                    type="text" 
                    placeholder="Enter email address" 
                    value={email} 
                    onChange={onChangeUserEmail}
                    autoComplete="off"
                    required
                    />
                </div>

                <div>
                    <label htmlFor="user-password"></label>
                    <textarea
                        cols="80"
                        rows="5"
                        value={password} 
                        onChange={onChangeUserPassword}
                        placeholder={"문의사항을 남겨주세요"}
                        autoComplete="off"
                     />
            <button>문의하기</button>
                </div>


                <Link to="/">돌아가기</Link>
            </RegisterForm>
        </>
    )
}
export default SendMain;

const RegisterForm = styled.form`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
    text-align: center;

    & h1 {
        color: #4F5681
    }

    & input {
        box-sizing: border-box;
        width: 50%;
        margin: 0.1rem 0;
        padding: 0.35rem;
        border: 1px solid #DDD;
        font-size: 0.875rem;
        color: #666;
    }

    & input::placeholder{
        font-size: 0.875rem;
        color: #ccc;
    }
    & textarea {
        box-sizing: border-box;
        width: 50%;
        margin: 0.1rem 0;
        padding: 0.35rem;
        border: 1px solid #DDD;
        font-size: 0.875rem;
        color: #666;
    }

    & textarea::placeholder{
        font-size: 0.875rem;
        color: #ccc;
    }

    & input:focus{
        outline: none;
        border: 1px solid #7784cc;
        box-shadow: 0 0 0 0.1rem rgb(59 65 99/ 25%);
    }

    & button {
        box-sizing: border-box;
        width: 50%;
        margin: 0.2rem;
        padding: 0.3rem 0;
        border: none;
        font-size: 0.875rem;
        color: #fff;
        background: #4F5681;
        cursor: pointer;
    }

    & button:hover {
        background: #3b4163;
    }

    & a {
        display: block;
        font-size: 0.875rem;
        color: #666;
    }
`

const CheckMessage = styled.p`
    width: 50%;
    margin: 0 auto;
    padding: 0;
    font-size: 0.875rem;
    color: red;
    text-align: left;
`