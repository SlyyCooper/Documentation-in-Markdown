## Table of Contents

- [How to Deploy to LangGraph Cloud¶](#how-to-deploy-to-langgraph-cloud)
  - [Prerequisites¶](#prerequisites)
  - [Create New Deployment¶](#create-new-deployment)
  - [Create New Revision¶](#create-new-revision)
  - [View Build and Server Logs¶](#view-build-and-server-logs)
  - [Interrupt Revision¶](#interrupt-revision)
  - [Delete Deployment¶](#delete-deployment)
  - [Deployment Settings¶](#deployment-settings)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to Deploy to LangGraph Cloud

Initializing search

GitHub

  * Home 
  * Tutorials 
  * How-to Guides 
  * Conceptual Guides 
  * Reference 

GitHub

  * Home 
  * Tutorials 
  * How-to Guides 

How-to Guides

    * LangGraph  LangGraph 
      * LangGraph 
      * Controllability 
      * Persistence 
      * Memory 
      * Human-in-the-loop 
      * Streaming 
      * Tool calling 
      * Subgraphs 
      * Multi-agent 
      * State Management 
      * Other 
      * Prebuilt ReAct Agent 
    * LangGraph Platform  LangGraph Platform 
      * LangGraph Platform 
      * Application Structure 
      * Deployment  Deployment 
        * Deployment 
        * How to Deploy to LangGraph Cloud  How to Deploy to LangGraph Cloud  Table of contents 
          * Prerequisites 
          * Create New Deployment 
          * Create New Revision 
          * View Build and Server Logs 
          * Interrupt Revision 
          * Delete Deployment 
          * Deployment Settings 
        * How to do a Self-hosted deployment of LangGraph 
        * How to interact with the deployment using RemoteGraph 
      * Authentication & Access Control 
      * Assistants 
      * Threads 
      * Runs 
      * Streaming 
      * Human-in-the-loop 
      * Double-texting 
      * Webhooks 
      * Cron Jobs 
      * LangGraph Studio 
    * Troubleshooting 

Troubleshooting

      * Troubleshooting 
      * GRAPH_RECURSION_LIMIT 
      * INVALID_CONCURRENT_GRAPH_UPDATE 
      * INVALID_GRAPH_NODE_RETURN_VALUE 
      * MULTIPLE_SUBGRAPHS 
  * Conceptual Guides 
  * Reference 

Table of contents

  * Prerequisites 
  * Create New Deployment 
  * Create New Revision 
  * View Build and Server Logs 
  * Interrupt Revision 
  * Delete Deployment 
  * Deployment Settings 

  1. Home 
  2. How-to Guides 
  3. LangGraph Platform 
  4. Deployment 

# How to Deploy to LangGraph Cloud¶

LangGraph Cloud is available within LangSmith. To deploy a LangGraph Cloud
API, navigate to the LangSmith UI.

## Prerequisites¶

  1. LangGraph Cloud applications are deployed from GitHub repositories. Configure and upload a LangGraph Cloud application to a GitHub repository in order to deploy it to LangGraph Cloud.
  2. Verify that the LangGraph API runs locally. If the API does not run successfully (i.e. `langgraph dev`), deploying to LangGraph Cloud will fail as well.

## Create New Deployment¶

Starting from the LangSmith UI...

  1. In the left-hand navigation panel, select `LangGraph Platform`. The `LangGraph Platform` view contains a list of existing LangGraph Cloud deployments.
  2. In the top-right corner, select `+ New Deployment` to create a new deployment.
  3. In the `Create New Deployment` panel, fill out the required fields.
    1. `Deployment details`
      1. Select `Import from GitHub` and follow the GitHub OAuth workflow to install and authorize LangChain's `hosted-langserve` GitHub app to access the selected repositories. After installation is complete, return to the `Create New Deployment` panel and select the GitHub repository to deploy from the dropdown menu. **Note** : The GitHub user installing LangChain's `hosted-langserve` GitHub app must be an owner of the organization or account.
      2. Specify a name for the deployment.
      3. Specify the desired `Git Branch`. A deployment is linked to a branch. When a new revision is created, code for the linked branch will be deployed. The branch can be updated later in the Deployment Settings.
      4. Specify the full path to the LangGraph API config file including the file name. For example, if the file `langgraph.json` is in the root of the repository, simply specify `langgraph.json`.
      5. Check/uncheck checkbox to `Automatically update deployment on push to branch`. If checked, the deployment will automatically be updated when changes are pushed to the specified `Git Branch`. This setting can be enabled/disabled later in the Deployment Settings.
    2. Select the desired `Deployment Type`.
      1. `Development` deployments are meant for non-production use cases and are provisioned with minimal resources.
      2. `Production` deployments can serve up to 500 requests/second and are provisioned with highly available storage with automatic backups.
    3. Determine if the deployment should be `Shareable through LangGraph Studio`.
      1. If unchecked, the deployment will only be accessible with a valid LangSmith API key for the workspace.
      2. If checked, the deployment will be accessible through LangGraph Studio to any LangSmith user. A direct URL to LangGraph Studio for the deployment will be provided to share with other LangSmith users.
    4. Specify `Environment Variables` and secrets. See the Environment Variables reference to configure additional variables for the deployment.
      1. Sensitive values such as API keys (e.g. `OPENAI_API_KEY`) should be specified as secrets.
      2. Additional non-secret environment variables can be specified as well.
    5. A new LangSmith `Tracing Project` is automatically created with the same name as the deployment.
  4. In the top-right corner, select `Submit`. After a few seconds, the `Deployment` view appears and the new deployment will be queued for provisioning.

## Create New Revision¶

When creating a new deployment, a new revision is created by default.
Subsequent revisions can be created to deploy new code changes.

Starting from the LangSmith UI...

  1. In the left-hand navigation panel, select `LangGraph Platform`. The `LangGraph Platform` view contains a list of existing LangGraph Cloud deployments.
  2. Select an existing deployment to create a new revision for.
  3. In the `Deployment` view, in the top-right corner, select `+ New Revision`.
  4. In the `New Revision` modal, fill out the required fields.
    1. Specify the full path to the LangGraph API config file including the file name. For example, if the file `langgraph.json` is in the root of the repository, simply specify `langgraph.json`.
    2. Determine if the deployment should be `Shareable through LangGraph Studio`.
      1. If unchecked, the deployment will only be accessible with a valid LangSmith API key for the workspace.
      2. If checked, the deployment will be accessible through LangGraph Studio to any LangSmith user. A direct URL to LangGraph Studio for the deployment will be provided to share with other LangSmith users.
    3. Specify `Environment Variables` and secrets. Existing secrets and environment variables are prepopulated. See the Environment Variables reference to configure additional variables for the revision.
      1. Add new secrets or environment variables.
      2. Remove existing secrets or environment variables.
      3. Update the value of existing secrets or environment variables.
  5. Select `Submit`. After a few seconds, the `New Revision` modal will close and the new revision will be queued for deployment.

## View Build and Server Logs¶

Build and server logs are available for each revision.

Starting from the `LangGraph Platform` view...

  1. Select the desired revision from the `Revisions` table. A panel slides open from the right-hand side and the `Build` tab is selected by default, which displays build logs for the revision.
  2. In the panel, select the `Server` tab to view server logs for the revision. Server logs are only available after a revision has been deployed.
  3. Within the `Server` tab, adjust the date/time range picker as needed. By default, the date/time range picker is set to the `Last 7 days`.

## Interrupt Revision¶

Interrupting a revision will stop deployment of the revision.

Undefined Behavior

Interrupted revisions have undefined behavior. This is only useful if you need
to deploy a new revision and you already have a revision "stuck" in progress.
In the future, this feature may be removed.

Starting from the `LangGraph Platform` view...

  1. Select the menu icon (three dots) on the right-hand side of the row for the desired revision from the `Revisions` table.
  2. Select `Interrupt` from the menu.
  3. A modal will appear. Review the confirmation message. Select `Interrupt revision`.

## Delete Deployment¶

Starting from the LangSmith UI...

  1. In the left-hand navigation panel, select `LangGraph Platform`. The `LangGraph Platform` view contains a list of existing LangGraph Cloud deployments.
  2. Select the menu icon (three dots) on the right-hand side of the row for the desired deployment and select `Delete`.
  3. A `Confirmation` modal will appear. Select `Delete`.

## Deployment Settings¶

Starting from the `LangGraph Platform` view...

  1. In the top-right corner, select the gear icon (`Deployment Settings`).
  2. Update the `Git Branch` to the desired branch.
  3. Check/uncheck checkbox to `Automatically update deployment on push to branch`.
    1. Branch creation/deletion and tag creation/deletion events will not trigger an update. Only pushes to an existing branch will trigger an update.
    2. Pushes in quick succession to a branch will not trigger subsequent updates. In the future, this functionality may be changed/improved.

## Comments

Back to top

Previous

Rebuild Graph at Runtime

Next

How to do a Self-hosted deployment of LangGraph

Made with  Material for MkDocs Insiders