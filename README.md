# Digital Ocean Route Icons - Function

A repository for deploying a function for generating route icons to be used with [Home Assistant GTFS Realtime](https://github.com/bcpearce/homeassistant-gtfs-realtime).

## Usage with Home Assistant GTFS Realtime

When setting up the integration, you can designate a URL for route icons.

This repository can deploy a function to Digital Ocean that can provide these icons.

In order to use, deploy the function using [Digital Ocean Functions](https://docs.digitalocean.com/products/functions/) set the URL to:

`https://path.to.digital-ocean-url.co/route-icons/svg-generator?text={}&color=%23{}&text_color=%23{}`

This will merge the route colors to those designated by the GTFS static data from your provider.