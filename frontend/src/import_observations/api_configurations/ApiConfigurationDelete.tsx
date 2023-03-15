import { useState } from "react";
import { Button, Confirm, useNotify, useRefresh, useDelete } from "react-admin";
import DeleteIcon from "@mui/icons-material/Delete";

type APIConfigurationDeleteProps = {
    api_configuration: any;
};

const APIConfigurationDelete = (props: APIConfigurationDeleteProps) => {
    const [open, setOpen] = useState(false);
    const [deleted, setDeleted] = useState(false);
    const [error_shown, setErrorShown] = useState(false);
    const [deleteOne, { isLoading, error }] = useDelete(); // eslint-disable-line @typescript-eslint/no-unused-vars
    // isLoading is not needed but easier to let it there
    const refresh = useRefresh();
    const notify = useNotify();
    const handleClick = () => setOpen(true);
    const handleDialogClose = () => setOpen(false);

    const handleConfirm = async () => {
        deleteOne("api_configurations", { id: props.api_configuration.id });
        setDeleted(true);
        refresh();
        setOpen(false);
    };

    if (error && !error_shown) {
        setErrorShown(true);
        setDeleted(false);
        notify("API configuration could not be deleted: " + error, {
            type: "warning",
        });
    } else if (deleted) {
        setDeleted(false);
        notify("API configuration deleted");
    }

    return (
        <>
            <Button
                label="Delete"
                onClick={handleClick}
                startIcon={<DeleteIcon />}
                sx={{ color: "#d32f2f" }}
            />
            <Confirm
                isOpen={open}
                title="Delete API configuration"
                content={
                    "Are you sure you want to delete the API configuration " +
                    props.api_configuration.name +
                    "?"
                }
                onConfirm={handleConfirm}
                onClose={handleDialogClose}
            />
        </>
    );
};

export default APIConfigurationDelete;
