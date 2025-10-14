import React from "react";
import Header from "../components/Header";

import Styles from "../styles/pages/Home.module.css";


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
                <button className={Styles.ctaButton}>Upload</button>
                <button className={Styles.ctaButton}>Apply Filter</button>
                <button className={Styles.ctaButton}>Draw Mode</button>
                <button className={Styles.ctaButton}>Download</button>
            </div>
        </div>
    </div>;
}