//실시간 검색어 기능 해당 기능은 더미데이터론 추축이 불가함 (db에서 최근검색을 추적해야 하는걸로 구상함)
import React from "react";
import {Link} from "react-router-dom";
import styled from "styled-components";


const SearchList = () => {
    return(

        <StyledWrap>
            <Link to="/searchresult">
            <p>검색결과를 간략하게 나타내는 컴포넌트 입니다. 반복적으로 쓰입니다.</p>
            </Link>
            <Link to="/searchresult">
            <p>검색결과를 간략하게 나타내는 컴포넌트 입니다. 반복적으로 쓰입니다.</p>
            </Link>
            <Link to="/searchresult">
            <p>검색결과를 간략하게 나타내는 컴포넌트 입니다. 반복적으로 쓰입니다.</p>
            </Link>
            <Link to="/searchresult">
            <p>검색결과를 간략하게 나타내는 컴포넌트 입니다. 반복적으로 쓰입니다.</p>
            </Link>
            <Link to="/searchresult">
            <p>검색결과를 간략하게 나타내는 컴포넌트 입니다. 반복적으로 쓰입니다.</p>
            </Link>
        </StyledWrap>
    )
}
export default SearchList;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
`
