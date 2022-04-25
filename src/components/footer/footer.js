import React from "react";
import styled from "styled-components";
import Banner from "../comp_public/banner";
import SearchSection from "../comp_public/searchsection";
import { useInput } from "../../hook/useInput";


const Footer = () => {
    const [keyword, onChangeKeyword] = useInput("");
    return(
        <>
            <StyledFC>
                <FooterMargin>
                    <h1><span>1푸터컨텐츠 (검색바)</span></h1>
                    
                    <p><span>homsquaredata_예시</span></p>
                    <p><span>홈스퀘어로</span></p>

                    <SearchTamplate>
                    <Blank/>
                    <div>
                        <label htmlFor="search-keyword"></label>
                        <input 
                        name="search-keyword"
                        type="text"
                        value={keyword}
                        onChange={onChangeKeyword}
                        placeholder="사업자번호를 입력해 주세요"
                        autoComplete="on"
                        required
                    />
                    <button>검색</button>
                    </div>
                    <div style={{
                        paddingTop: '1rem',
                        color: '#fff',
                        float: "left"
                    }}>
                        Copyright ©2022 All rights reserved
                    </div>
                    </SearchTamplate>
                </FooterMargin>
                <FooterMargin>
                    <p><span>2푸터컨텐츠</span></p>
                    <p style={{color : '#fff'}}>길이확인길이확인길이확인길이확인길이확인</p>
                    
                    
                </FooterMargin>
            </StyledFC>
        </>

        
    )
}
export default Footer;


const Blank = styled.div`
    min-height: 3rem;
    `
const FooterMargin = styled.div`
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #a0a0a0;

`
const FooterMarginL = styled.div`
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #a0a0a0;
    float: left;

`
const whiteP = styled.p`
    padding-top: 1rem;
    color: '#fff';
    float: "left"
`

const StyledFC = styled.div`
    display: flex;
    justify-content: space-around;

    box-sizing: border-box;
    max-width: 60%;
    min-width: 100rem;
    width: 80%;
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #a0a0a0;

    & a {
        padding-top: 0.3rem;
        text-decoration: none;
        font-size: 0.875rem;
        color: #666;
        cursor: pointer;
    }

    & span {
        font-size: 1.5rem;
        font-weight: 900;
        color: #fff;
        cursor: pointer;
        :hover {
            color: #8f8f8f;
        }
    }
    
    & button {
        border: none;
        padding-top: 0.3rem;
        font-size: 0.875rem;
        color: #666;
        background: none;
        cursor: pointer;

        :hover {
            color: #8f8f8f;
        }
    }

`
const SearchTamplate = styled.div`
    box-sizing: border-box;
    max-width: 100rem;
    min-width: 30rem;
    width: 80%;
    height: 6rem;
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
        color: #a0a0a0;
    }

    & input:focus{
        outline: none;
        border: 1px solid #7784cc;
        box-shadow: 0 0 0 0.1rem rgb(59 65 99/ 25%);
    }

    & button {
        box-sizing: border-box;
        width: 20%;
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