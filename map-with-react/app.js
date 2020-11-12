import React, {Component, Fragment} from "react";

import {
    withScriptjs,
    withGoogleMap,
    GoogleMap,
    Marker,
    Polyline
} from "react-google-maps";


class MapApp extends Component {
    static defaultProps = {
        googleMapURL: "https://maps.googleapis.com/maps/api/js?key=<KEY>&v=3.exp&libraries=geometry,drawing,places",
    }

    points = []

    mapOnClick = (props) => {
        this.points.push({lat: props.latLng.lat(), lng: props.latLng.lng()})
        this.setState({
            polygon_points: this.points,
            marker_point: {lat: props.latLng.lat(), lng: props.latLng.lng()},
            markers: this.points
        });
        let str = "";
        for (let i = 0; i < this.points.length; i++) {
            str += "coordinates.emplace_back(util::FloatLongitude{" + this.points[i].lng + "}, util::FloatLatitude{" + this.points[i].lat + "}); \n"
        }
        document.getElementById("root").textContent = str
    }

    MapWithScript = withScriptjs(withGoogleMap(props =>
        <GoogleMap
            defaultZoom={15}
            defaultCenter={{lat: 12.874654, lng: 77.670559}}
            onClick={this.mapOnClick}>
            {props.children}
        </GoogleMap>
    ));

    componentWillMount = () => {
        this.setState({
            polygon_points: [],
            marker_point: {lat: 12.874654, lng: 77.670559},
            my_points: []
        })
    };

    render() {
        const markers = [];
        for (let i = 0; i < this.state.polygon_points.length; i++) {
            markers.push(<Polyline path={this.state.polygon_points} draggable={true}/>);
        }
        return (
            <this.MapWithScript
                googleMapURL={this.props.googleMapURL}
                loadingElement={<div style={{height: `100%`}}/>}
                containerElement={<div style={{height: `700px`}}/>}
                mapElement={<div style={{height: `100%`}}/>}
                center={{lat: 12.874654, lng: 77.670559}}>
                <Marker position={this.state.marker_point}/>
                {markers}
                <Polyline path={this.state.my_points} draggable={true}/>
            </this.MapWithScript>
        )
    };
}

export default MapApp;
