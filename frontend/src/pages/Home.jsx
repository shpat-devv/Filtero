import React from "react";
import Header from "../components/Header";
import FileUploader from "../components/FileUploader";

import Styles from "../styles/pages/Home.module.css";


function handleApplyFilterClick() {
    console.log("Apply Filter button clicked");
}

function handleDrawModeClick() {
    console.log("Draw Mode button clicked");
}

function handleDownloadClick() {
    console.log("Download button clicked");
}

export default function HomePage() {
    return <div className={Styles.homePageContainer}>
        <Header
            title="Filtero"
            subtitle="Filter any image to your desire"
            buttonText="Pages"
            menuItems={[
                { title: "Home", link: "/" },
                { title: "About", link: "/about" },
                { title: "Contact", link: "/contact" }
            ]}
        />
        <div className="spacer"></div>
        <div className={Styles.content}>
            <div className={Styles.contentLeft}>
                <img className={Styles.homeContentImage} src="default.jpeg" alt="image" />
            </div>
            <div className={Styles.contentRight}>
                <FileUploader />
                <button className={Styles.ctaButton} onClick={handleApplyFilterClick}>Apply Filter</button>
                <button className={Styles.ctaButton} onClick={handleDrawModeClick}>Draw Mode</button>
                <button className={Styles.ctaButton} onClick={handleDownloadClick}>Download</button>
            </div>
        </div>
    </div>;
}