// 검색바 관련 섹션 
import React from "react";
import {Link} from "react-router-dom";
import styled from "styled-components";
import { useInput } from "../../hook/useInput";


const SearchSectionFooter = () => {
    const [email, onChangeEmail] = useInput("");
    return(
        <StyledWrap>
            <Blank/>
            <Styledbar>
                <h1>사업자등록번호 조회</h1>
            </Styledbar>
            <Styledbar>
                <h3>사업자등록번호로  사업자정보</h3>
            </Styledbar>
            <Styledbar>
                <h2>Total : 3,455,422</h2>
            </Styledbar>
            <SearchTamplate>
                <p>검색바 위치자리</p>
                <div>
                    <label htmlFor="user-email"></label>
                    <input 
                    name="user-email"
                    type="text"
                    value={email}
                    onChange={onChangeEmail}
                    placeholder="사업자번호를 입력해 주세요"
                    autoComplete="on"
                    required
                    />
                    <button>검색</button>
                </div>
            </SearchTamplate>
            <Blank/>

            <Blank/>
        </StyledWrap>
    )
}
export default SearchSectionFooter;

const StyledWrap = styled.div`
    box-sizing: border-box;

    min-width: 18.75rem;
    min-height: 18.75rem;
    width: 100%;
    height: 100%;
    margin: 0 auto;
    background-color: #666;
    background: url(https://source.unsplash.com/random/1920x1080);
    background-size: cover;
`
const Styledbar = styled.div`
    box-sizing: border-box;
    min-height: 5rem;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 100%;
    height: 100%;
    margin: 0 auto;
    padding: 10rem auto;
    color: #efefef;

    display: flex;
    justify-content: center;
    align-items: center;
    white-space: pre-line;


`
const Blank = styled.div`
    min-height: 2rem;
`
const SearchTamplate = styled.div`
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
        width: 70%;
        height: 2.5rem;
        border-radius: 15px;
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

    & input:focus{
        outline: none;
        border: 1px solid #7784cc;
        box-shadow: 0 0 0 0.1rem rgb(59 65 99/ 25%);
    }

    & button {
        box-sizing: border-box;
        width: 10%;
        height: 2.5rem;
        border-radius: 15px;
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