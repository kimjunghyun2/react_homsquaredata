import React from "react";
import styled from "styled-components";


const SearchLog = () => {
    return(
        <StyledWrap>
            <p>실시간 검색어 입니다 지금은 li ul을 사용합니다.</p>
            <ul>
                <h1>실시간 검색어</h1>
                <StyledList><a>검색어1</a></StyledList>
                <StyledList><a>검색어2</a></StyledList>
                <StyledList><a>검색어3</a></StyledList>
                <StyledList><a>검색어4</a></StyledList>
                <StyledList><a>검색어5</a></StyledList>
            </ul>
            <p>원래는 이곳도 더미데이터와 맵함수를 써야 합니다.</p>
        </StyledWrap>
    )
}
export default SearchLog;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 15rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
    float: right;
`

const StyledList = styled.li`
    text-align: center;

    &a{
        justify-content: flex-end;
    }
`
