module.exports = async function (context, req) {
    const isInsideGeofence = req.body.inside; 

    if (isInsideGeofence) {
        context.bindings.message = {
            to: "+840377532125", 
            from: "+17018922157", 
            body: "Device is inside the geofence."
        };
    }

    context.res = {
        status: 200,
        body: "Notification sent."
    };
};
