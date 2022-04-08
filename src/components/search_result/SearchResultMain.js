import React from "react";
import styled from "styled-components";


const SearchResultMain = () => {
    return(
        <StyledWrap>
            <p>검색 상세 창입니다. 표만드는 기능을 사용할 수도 있습니다</p>
        </StyledWrap>
    )
}
export default SearchResultMain;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
`