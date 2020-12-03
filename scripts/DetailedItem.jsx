import React from "react";
import Socket from "./Socket";
import LineGraph from "./LineGraph";
import ProfileButton from "./ProfileButton";
import CommentsSection from "./CommentsSection";
import LikeSection from "./LikeSection";
import { Link } from "react-router-dom";
import "../style/DetailedItem.css";

export default function DetailedView(props) {
  function handleBack(e) {
    Socket.emit("go back");
  }
  return (
    <div>
      <Link to="/" onClick={handleBack}>
        {" "}
        Go back to searches{" "}
      </Link>{" "}
      <br />
      <div className={"more-info-box"}>
          <h1>Historical Price</h1> <br />
          <ol className="priceList">
            {props.dataset.map((date, index) => (
              <li key={date}>
                {props.dataset[index]} - ${props.datapts[index]}
              </li>
            ))}
          </ol>
          <h2>Visualization Graph</h2> <br />
          <LineGraph
            className="graphcanvas"
            datapts={props.datapts}
            dataset={props.dataset}
          />
          Mean: {props.mean} <br />
          Variance: {props.variance} <br />
          Historical low: ${props.min} <br />
          Historical high: ${props.max} <br />
          Posted by:
          <ProfileButton
            activeOnlyWhenExact={true}
            to={"/profile/" + props.user}
            label={props.user}
            username={props.user}
          />{" "}
          <img className="user-photo" src={props.pfp} alt={props.user} />
          <LikeSection
            username={props.username}
            postID={props.postOf}
          />
          <a href={"https://www.amazon.com/dp/" + props.asin}>Buy it on Amazon!</a>
          <CommentsSection
            username={props.user}
            pfp={props.pfp}
            postID={props.postOf}
          />
      </div>

    </div>
  );
}
