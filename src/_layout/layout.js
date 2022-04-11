// j쿼리와 부트스트랩 그냥 박아놓고 시작하고 싶다.
//
import React from "react";
import styled from "styled-components";
import {Link} from "react-router-dom";
import Footer from "../components/footer/footer";
import Banner from "../components/comp_public/banner";

const Layout = ({children}) => {
    return (
        <>
            <StyledNavDiv>
            <StyledNav>
                <div>
                    <Link to="/">
                        <span>homsquaredata_예시</span>
                    </Link>
                </div>
                <div>
                    <a onClick={()=>window.open('https://homesquare.co.kr','_blank')}>
                    <span>홈스퀘어로</span>
                    </a>
                </div>
            <StyledInfo>
                +@
            </StyledInfo>
            </StyledNav>
            </StyledNavDiv>
            <StyledMain>
            <section>
            </section>
            <div>{children}</div>
   
            </StyledMain>
            <StyledFooter>
                <Footer/>
            </StyledFooter>
        </>
    )
}
export default Layout;

const StyledNavDiv = styled.div`
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #fcc513;

`

const StyledNav = styled.div`
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #fcc513;

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
        color: #4f5681;
    }
`

const StyledFooter = styled.div`
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    box-sizing: border-box;

    width: 100%;
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #a0a0a0;

    & a {
        padding-top: 0.3rem;
        text-decoration: none;
        font-size: 0.875rem;
        color: #666;
    }

    & span {
        font-size: 1.5rem;
        font-weight: 900;
        color: #fff;
    }

    & p {
        width: 80%;
        color: #fff;
    }

`
const StyledMain = styled.div`
    min-height: calc(100vh - 180px);
`
const StyledInfo = styled.div`
    font-size: 0.875rem;
    color: #666;
    cursor: default;

    & button {
        border: none;
        padding-top: 0.3rem;
        font-size: 0.875rem;
        color: #666;
        background: none;
        cursor: pointer;

        :hover {
            color: #000;
        }
    }
`
