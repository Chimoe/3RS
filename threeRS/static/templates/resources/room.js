document.addEventListener("DOMContentLoaded", function() {
    new FancyGrid({
        title: 'Row edit',
        renderTo: 'container',
        width: 1000,
        height: 400,
        data: data,
        defaults: {
            type: 'string',
            width: 100,
            editable: false,
            sortable: false,
            resizable: false,
            ellipsis: false
        },
        clicksToEdit: 1,
        rowEdit: false,
        columns: [{
            index: 'id',
            title: 'ID',
            type: 'number',
            editable: false,
            width: 100
        }, {
            index: 'name',
            title: 'Name',
            width: 450
        }, {
            index: 'requested',
            title: 'Requested',
            type: 'checkbox',
            width: 450
        }, ]
    });
});

var data = [{
    id: 1,
    name: 'DCC 308',
    requested: false,
}, {
    id: 2,
    name: 'DCC 318',
    requested: false,
}, {
    id: 3,
    name: 'Amos Eaton 127',
    requested: true,
}, {
    id: 4,
    name: 'Amos Eaton 115',
    requested: false,
}, {
    id: 5,
    name: 'Sage 3303',
    requested: true,
}, {
    id: 6,
    name: 'Sage 4510',
    requested: false,
}, {
    id: 7,
    name: 'Lally 307',
    requested: true,
}, {
    id: 8,
    name: 'Troy 3031',
    requested: false,
}, {
    id: 9,
    name: 'McNeil',
    requested: false,
}];