import React, { useCallback, useState } from "react"
import {Link} from "react-router-dom";
import styled from "styled-components";
import { useInput } from "../../hook/useInput";

const RegisterMain = () => {
    const [email,onChangeUserEmail] = useInput("");
    const [name, onChangeUserName] = useInput("");
    const [content, onChangeContent] = useInput("");



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
                    <label htmlFor="user-content"></label>
                    <textarea
                        cols="80"
                        rows="20"
                        value={content} 
                        onChange={onChangeContent}
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
export default RegisterMain;

const RegisterForm = styled.form`
    box-sizing: border-box;

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
        border-radius: 10px;
    }

    & input::placeholder{
        font-size: 0.875rem;
        color: #ccc;
    }
    & textarea {
        box-sizing: border-box;
        border-radius: 10px;
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
        border-radius: 15px;
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

